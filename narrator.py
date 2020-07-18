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

from bs4 import BeautifulSoup as bs
import requests

## Get page html
def getWikiHTML():
  urlBase = "https://darkestdungeon.gamepedia.com/Narrator"
  response = requests.get(urlBase).content
  soup = bs(response,'html.parser')
  return soup

#### Table of Contents
# Get table of content
def get_table_of_content(soup, html=False):
  toc_html = soup.find('div',{"class":"toc"})
  list_a = toc_html.find_all('a')
  if html:
    return list_a
  else:
    toc = {}
    for elem in list_a:
      number = elem.find('span',{'class':'tocnumber'}).contents[0]
      text = elem.find('span',{'class':'toctext'}).contents[0]
      toc[number] = text
    return toc

#### Contents
## Quotes AND Audio Sources
# Get quotes and audio sources
def get_quotes_audios(soup, html=False):
  quotes_audios_html = soup.find('div',{"class":"mw-parser-output"})
  list_table_and_audio = quotes_audios_html.find_all(['table','audio'])
  if html:
    return list_table_and_audio
  else:
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
def get_quotes(soup, html=False):
  quotes_html = soup.find('div',{"class":"mw-parser-output"})
  list_table = quotes_html.find_all('table')
  if html:
    return list_table
  else:
    quotes = []
    for elem in list_table:
      quote = elem.find('i').contents[0]
      quotes.append(quote)
    return quotes

## Audio Sources
# Get audios
def get_audios(soup, html=False):
  audios_html = soup.find('div',{"class":"mw-parser-output"})
  list_audio = audios_html.find_all('audio')
  if html:
    return list_audio
  else:
    audios = []
    for elem in list_audio:
      source = elem.find('source').attrs['src']
      audios.append(source)
    return audios



# Get narrator lines
# currently only accepts one at a time
def narrator(toc=False, quotes=False, audios=False, download=False, html=False):
  soup = getWikiHTML()
  if toc:
    info = get_table_of_content(soup, html)
  elif quotes and audios:
    info = get_quotes_audios(soup, html)
  elif quotes:
    info = get_quotes(soup, html)
  elif audios:
    info = get_audios(soup, html)
  else: # quotes and audio sources is the default
    info = get_quotes_audios(soup, html)
  return info

if __name__ == "__main__":
  info = narrator(toc=True)
  # info = narrator(toc=True, html=True)
  # info = narrator(quotes=True, audios=True)
  # info = narrator(quotes=True)
  # info = narrator(audios=True)
  print(info)
