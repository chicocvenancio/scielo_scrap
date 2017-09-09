# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
import requests
import sys


def main(argv):
    response = requests.get(argv[1])
    soup = BS(response.text, 'html')
    [sup.extract() for sup in soup.find_all('sup')]
    print(soup.find('div', {'class':'index,pt'}).get_text().split(u'Introdução')[1].split(u'Referências')[0])

if __name__ == "__main__":
   main(sys.argv[1:])