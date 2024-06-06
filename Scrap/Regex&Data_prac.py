import requests as rq
from bs4 import BeautifulSoup
import re

url = 'https://books.toscrape.com/'

resp = rq.get(url)
bSoup = BeautifulSoup(resp.content, "html.parser")

Heading = bSoup.findAll(text='Books to')

print(Heading)

Travel = bSoup.findAll(text='Travel')

print(f'Travel ={Travel}')

re.compile("Fiction", re.I)

original_text = bSoup.findAll(text=re.compile("Fiction", re.I))

print(original_text[1].strip())

Fictions_name = [textData.strip() for textData in original_text]

print(Fictions_name)