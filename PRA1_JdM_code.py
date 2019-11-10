# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es el archivo PRA1_JdM_code.
"""

# Importamos librerías Python que usaremos.
import requests
import csv
from bs4 import BeautifulSoup

# Creamos tabla para guardar las url's a acceder
web_pages = []
# Grabamos en la tabla la url de las webs que deseamos acceder.
url_page = 'https://www.espinaler.com/es/producto-espinaler/almeja-blanca'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/almeja-extra'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/almeja-natural'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/atun'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/berberecho'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/bonito'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/caracol-de-mar'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/chipiron'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/erizo'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/langostillo'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/mejillon'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/navaja'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/pulpo'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/rodaja-de-pulpo'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/sardina'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/sardinilla'
web_pages.append(url_page)
url_page = 'https://www.espinaler.com/es/producto-espinaler/zamburina'
web_pages.append(url_page)

cabecera = "Producto"
catalog = []
headerCatalog = cabecera
catalog.append(headerCatalog)

for a in web_pages:
# Hacemos el request a la página web.
    page = requests.get(a).text
# Procesamos el HTML mediante un objeto BeutifulSoup
    soup = BeautifulSoup(page, 'html.parser')
    for text in soup.find_all('h4'):
        texto = list(text)
        print(texto[0])
        catalog.append(texto[0])

# Abrimos el fichero y grabamos la información.
with open('PRA1_JdM.csv', 'w', newline = '') as csv_file:
    writer = csv.writer(csv_file)
    for text in catalog:    
        writer.writerow([text])