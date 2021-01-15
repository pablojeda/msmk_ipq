import os
import sys
import django
import requests
from bs4 import BeautifulSoup

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.append(root)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "varianza.settings.development")
django.setup()

if __name__ == '__main__':
    link = 'https://playtomic.io/rio-arena-padel/da766fd6-43b3-11e8-8674-52540049669c?q=PADEL~%s~%s~~'
    html = requests.get(link)
    soup = BeautifulSoup(html.content, 'html.parser')
    marcador = False
    for fila in soup.find_all('tr'):
        if fila.find('th'):
            if 'Ejercicio' in fila.find('th').contents:
                marcador = True
                continue
        if marcador:
            href = fila.find_all('td')[-1].find('a', href=True)['href']
            celda = 'A%s' % i
            print('Metiendo link ------- %s -------- en fila %s' % (href.split('/')[2:], i))
            ws1[celda] = 'http://www.cnmv.es/Portal/' + ''.join(href.split('/')[2:])
            break
