import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://yandex.ru/news'
with requests.Session() as s:
             r = s.get(url)

options = webdriver.Chrome()
options.get(url)
text=options.page_source

d=[]
s=[] 

r.encoding='utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a')[28:38]:
    d.append({'title':link.get_text(),
            'href':link.get('href')})
print(d)
for i in d:
    for key,item in i.items():
        s.append(item)
StrA = "\n".join(s)
print(s)