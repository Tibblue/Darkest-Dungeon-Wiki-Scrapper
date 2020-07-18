from bs4 import BeautifulSoup as BS
import requests

# get page html
def getHTML():
  urlBase = "https://darkestdungeon.gamepedia.com/Narrator"
  response = requests.get(urlBase).content
  soup = BS(response,'html.parser')
  return soup

#### Table of Contents
# get table of content from Soup
def get_table_of_content(soup):
  toc = soup.find('div',{"class":"toc"})
  toc = parse_toc(toc)
  return toc

# parse ToC HTML to dict
def parse_toc(html):
  toc = {}
  list_a = html.find_all('a')
  for elem in list_a:
    number = elem.find('span',{'class':'tocnumber'}).contents[0]
    text = elem.find('span',{'class':'toctext'}).contents[0]
    toc[number] = text
  return toc

#### Contents
# get content from Soup
def get_content(soup):
  content = soup.find('div',{"class":"mw-parser-output"})
  # remove toc from content
  content.find('div',{"class":"toc"}).decompose()

  # remove TABLE from content TEMP
  # for table in content.find_all('table'):
  #   table.decompose()

  content = parse_content(content)
  return content

# parse content HTML to dict
def parse_content(html):
  # list_table = html.find_all('table')
  # quotes = []
  # for elem in list_table:
  #   quote = elem.find('i').contents[0]
  #   quotes.append(quote)
  # return quotes

  # list_audio = html.find_all('audio')
  # audios = []
  # for elem in list_audio:
  #   source = elem.find('source').attrs['src']
  #   audios.append(source)
  # return audios

  list_table_and_audio = html.find_all(['table','audio'])
  content = {}
  last_quote = ''
  for elem in list_table_and_audio:
    if elem.name=='table':
      last_quote = elem.find('i').contents[0]
      content[last_quote] = []
    if elem.name=='audio':
      source = elem.find('source').attrs['src']
      content[last_quote].append(source)
  return content


# # cria a dic com uma palavra
# def create_dic(word,lista_soup):
#   palavras = []
#   for i in reversed(range(len(lista_soup))):
#     num_silabas = lista_soup[i].find('div',{'class':'row wordsBlock'})['n'].split()[0]
#     lista_palavras = lista_soup[i].find('div',{'class':'row wordsBlock'})
#     for html_palavra in lista_palavras:
#         palavra = html_palavra.string
#         if word != palavra:
#           palavras.append(palavra)
#   return palavras

# get narrator lines
# currently only accepts one at a time
def narrator_lines(toc=False, content=False):
  soup = getHTML()
  if toc:
    info = get_table_of_content(soup)
  # elif content:
  #   info = get_content(soup)
  else: # content is the default
    info = get_content(soup)
  return info

if __name__ == "__main__":
  # info = narrator_lines()
  info = narrator_lines(toc=True)
  # info = narrator_lines(content=True)
  print(info)
