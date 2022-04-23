from os import write
import requests
from bs4 import BeautifulSoup
import csv


URL = 'http://www.regtorg.ru/comps/skladskie-uslugi/page2.htm'
HEADERS = { 'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36',
            'accept': '*/*'}
FILE = 'sklad.csv'


def get_html(url,params=None):
    r=requests.get(url, headers=HEADERS)
    return r
 
def save_file(items,path):
    with open(path,'w',newline='',encoding='"utf-8-sig"') as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerow(['Название склада','Город склада','Текст склада','Адрес'])
        for item in items:
             writer.writerow([item['title'],item['sec_title'],item['text'],item['adres']])


def get_content(html):
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find_all('div',class_='compList')
    sklad = []
    sklad2 = []
    for item in items:
        k=item.find_all('div',class_='item')
        for i in k:
            j=i.find('p',class_='contact').get_text()
            sklad.append(
                {
                'title':i.find('h2',itemprop="name").get_text(strip=True),
                'sec_title':i.find('p',class_='city').get_text(),
                'text':i.find('p',class_='').get_text(strip=True),
                'adres':j
                }
        )
    sklad2.extend(sklad)
    print(sklad)
    print(len(sklad))
    return sklad2
    


def parse():
    URL = 'http://www.regtorg.ru/comps/skladskie-uslugi/'
    html=get_html(URL)
    i=2
    go=[]
    while i<27:
        go.extend(get_content(html.text)) 
        URL='http://www.regtorg.ru/comps/skladskie-uslugi/page'+str(i)+'.htm'
        html=get_html(URL)
        i+=1
        print("Парс пошел: ",URL)
    save_file(go,FILE)
parse()