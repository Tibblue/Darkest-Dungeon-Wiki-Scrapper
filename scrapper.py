#!/usr/bin/python3
"""Darkest Dungeon Wiki - Narrator Page Scrapper

  Scraps Narrator page.
  Currently can scrap:
    -Table of Content (HTML, Dict)
    -Quotes and Audio Sources (HTML List, Dict)
      -HTML List has reesults ordered by appearance,
        but doesn't associate a quote to its audio
      -Dict uses the Quote as the key, and a list of Audio Sources as value
    -Quotes (HTML List, List)
    -Audio Sources (HTML List, List)

"""

from bs4 import BeautifulSoup as BS
import requests

## Get page html
def getHTML():
  urlBase = "https://darkestdungeon.gamepedia.com/Narrator"
  response = requests.get(urlBase).content
  soup = BS(response,'html.parser')
  return soup

#### Table of Contents
# Get table of content
def get_table_of_content(soup):
  toc = soup.find('div',{"class":"toc"})
  toc = parse_toc(toc)
  return toc

# parse ToC HTML to Dict
def parse_toc(html):
  toc = {}
  list_a = html.find_all('a')
  for elem in list_a:
    number = elem.find('span',{'class':'tocnumber'}).contents[0]
    text = elem.find('span',{'class':'toctext'}).contents[0]
    toc[number] = text
  return toc

#### Contents
## Quotes AND Audio Sources
# Get quotes and audio sources
def get_quotes_audios(soup):
  quotes_audios = soup.find('div',{"class":"mw-parser-output"})
  quotes_audios = parse_quotes_audios(quotes_audios)
  return quotes_audios

# parse quotes and audio sources HTML to Dict
def parse_quotes_audios(html):
  list_table_and_audio = html.find_all(['table','audio'])
  quotes_audios = {}
  last_quote = ''
  for elem in list_table_and_audio:
    if elem.name=='table': # quote
      last_quote = elem.find('i').contents[0]
      quotes_audios[last_quote] = []
    if elem.name=='audio': # audio
      source = elem.find('source').attrs['src']
      quotes_audios[last_quote].append(source)
  return quotes_audios

## Quotes
# Get quotes
def get_quotes(soup):
  quotes = soup.find('div',{"class":"mw-parser-output"})
  quotes = parse_quotes(quotes)
  return quotes

# parse quotes HTML to Dict
def parse_quotes(html):
  list_table = html.find_all('table')
  quotes = []
  for elem in list_table:
    quote = elem.find('i').contents[0]
    quotes.append(quote)
  return quotes

## Audio Sources
# Get audios
def get_audios(soup):
  audios = soup.find('div',{"class":"mw-parser-output"})
  audios = parse_audios(audios)
  return audios

# parse audios HTML to Dict
def parse_audios(html):
  list_audio = html.find_all('audio')
  audios = []
  for elem in list_audio:
    source = elem.find('source').attrs['src']
    audios.append(source)
  return audios



# Get narrator lines
# currently only accepts one at a time
def narrator(toc=False, quotes=False, audios=False, download=False):
  soup = getHTML()
  if toc:
    info = get_table_of_content(soup)
  elif quotes and audios:
    info = get_quotes_audios(soup)
  elif quotes:
    info = get_quotes(soup)
  elif audios:
    info = get_audios(soup)
  else: # quotes and audio sources is the default
    info = get_quotes_audios(soup)
  return info

if __name__ == "__main__":
  # info = narrator()
  info = narrator(toc=True)
  # info = narrator(content=True)
  print(info)
