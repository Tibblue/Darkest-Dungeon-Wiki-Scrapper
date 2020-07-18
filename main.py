#!/usr/bin/python3
from random import choice
import scrapper
import argparse, sys
import regex as re

# output = None

# writes output to file or stdout
def write_output(output, info):
  info = str(info)
  output.write("\nOUTPUT\n"+info+'\n')

def main():
  global output
  parser = argparse.ArgumentParser()
  # parser.add_argument('-n','--rima', type=int,help='Número de rimas')
  parser.add_argument('-o','--output', type=str,help='Ficheiro de output')
  args = vars(parser.parse_args())

  if args['output'] is None: out = None
  else: out = args['output']

  # select output
  if out:
    output = open(out,'w+')
  else:
    output = sys.stdout

  # get info (narrator lines)
  # info = scrapper.narrator_lines(toc=True)
  info = scrapper.narrator_lines(content=True)

  # write info obtained
  write_output(output, info)

if __name__ == "__main__":
  main()
