#!/usr/bin/python3
"""Darkest Dungeon Wiki Scrapper

  Scraps Darkest Dungeon Wiki for info and file sources.
  Use --help to show the possible flags and their use.

  Note: This won't scrap literally everything.
        Small parts will be added one at a time.

"""

from random import choice
import narrator
import argparse, sys
import regex as re


def main():
  global output
  parser = argparse.ArgumentParser(description='Darkest Dungeon Wiki Scrapper.\nSelect the desired page and details to scrap using the arguments below.')
  ## Global arguments
  parser.add_argument('-o','--output', type=str, help='Output File')
  # parser.add_argument('-d','--download', action='store_true', help='Download all scraped Audio/Image sources (from the scraped results, in any page)')
  parser.add_argument('--html', action='store_true', help='Scrap all request elements, but leave them in their original HTML parts.')
  ## Page selector arguments
  parser.add_argument('-n','--narrator', action='store_true', help='Scrap Narrator Page (default: scraps quotes and audio source)')
  parser.add_argument('--toc', action='store_true', help='Scrap Table of Contents (from Narrator Page)')
  parser.add_argument('--quotes', action='store_true', help='Scrap Narrator Quotes (from Narrator Page)')
  parser.add_argument('--audios', action='store_true', help='Scrap Audio Source Links (from Narrator Page)')
  args = vars(parser.parse_args())

  ## Global arguments parse
  # select output
  if args['output']:
    output = open(args['output'],'w+')
  else:
    output = sys.stdout
  # HTML mode
  if args['html']:
    html = True
  else:
    html = False


  ## Select user scrap request
  # Only one page can be scraped at a time.
  # Some requests on the same page can be merged.
  if args['narrator']: # Narrator page (default: scrap quotes and audio sources)
    if args['toc']: # Scrap Table of Contents
      info = narrator.narrator(toc=True, html=html)
    elif args['quotes'] and args['audios']:
      info = narrator.narrator(quotes=True, audios=True, html=html)
    elif args['quotes']:
      info = narrator.narrator(quotes=True, html=html)
    elif args['audios']:
      info = narrator.narrator(audios=True, html=html)
    else: # Scrap content (quotes and audio sources, html=html)
      info = narrator.narrator(quotes=True, audios=True, html=html)
  else:
    info = "Please select a page to scrap."

  # write info obtained to output
  info = str(info) # for safety
  print(info, file=output)

if __name__ == "__main__":
  main()
