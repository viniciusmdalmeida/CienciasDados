import requests
from bs4 import BeautifulSoup

class WebScrapping():
    link = 'https://lista.mercadolivre.com.br/'

    def __init__(self):
        pass

    def buscar(self,item):
        item = item.replace(' ','-')
        text = requests.get(self.link+item).text
        soup = BeautifulSoup(text, 'html.parser')

        listaSaida = soup.findAll('div', class_='item__info-container')
