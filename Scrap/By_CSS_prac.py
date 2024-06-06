import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://books.toscrape.com/'

resp = rq.get(url)

bSoup = BeautifulSoup(resp.content, "html.parser")

titlesTags = bSoup.select("article.product_pod > h3 > a")

print(titlesTags)

titles = [tag['title'] for tag in titlesTags]

print(titles)

print(bSoup.select('[title*=Woman]'))


allTitle = pd.DataFrame(titles)


print(allTitle)


allTitle.to_csv('title_list.csv', header=True, index=False)