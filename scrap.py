from bs4 import BeautifulSoup as BS
import requests

response = requests.get('http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0101-60832013000300005&lng=en&nrm=iso&tlng=pt')
soup = BS(response.text)
[sup.extract() for sup in soup.find_all('sup')]
print(soup.find('div', {'class':'index,pt'}).get_text().split('Introdução')[1].split('Referências')[0])