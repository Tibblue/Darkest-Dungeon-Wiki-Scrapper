#!/usr/bin/python3
"""Darkest Dungeon Wiki Scrapper

  Scraps Darkest Dungeon Wiki for info and file sources.
  Use --help to show the possible flags and their use.

  Note: This won't scrap literally everything.
        Small parts will be added one at a time.

"""

from random import choice
import scrapper
import argparse, sys
import regex as re


def main():
  global output
  parser = argparse.ArgumentParser(description='Darkest Dungeon Wiki Scrapper.\nSelect the desired page and details to scrap using the arguments below.')
  ## Global arguments
  parser.add_argument('-o','--output', type=str, help='Ficheiro de output')
  # parser.add_argument('-d','--download', type=str,help='Download all scraped Audio/Image sources (from the scraped results, in any page)')
  ## Page selector arguments
  parser.add_argument('-n','--narrator', action='store_true', help='Scrap Narrator Page (default: scraps quotes and audio source)')
  parser.add_argument('--toc', action='store_true', help='Scrap Table of Contents (from Narrator Page)')
  # parser.add_argument('--quotes', action='store_true', help='Scrap Narrator Quotes (from Narrator Page)')
  # parser.add_argument('--audio', action='store_true', help='Scrap Audio Source Links (from Narrator Page)')
  args = vars(parser.parse_args())

  ## Global arguments parse
  # select output
  if args['output'] is None:
    output = sys.stdout
  else:
    output = open(args['output'],'w+')

  ## Select user scrap request
  # Only one page can be scraped at a time.
  # Some requests on the same page can be merged.
  if args['narrator']: # Narrator page (default: scrap quotes and audio sources)
    if args['toc']: # Scrap Table of Contents
      info = scrapper.narrator(toc=True)
    # TODO add more options with arguments
    else: # Scrap content (quotes and audio sources)
      info = scrapper.narrator(content=True)
  else:
    info = "Please select a page to scrap."

  # write info obtained to output
  info = str(info) # for safety
  print(info, file=output)

if __name__ == "__main__":
  main()
