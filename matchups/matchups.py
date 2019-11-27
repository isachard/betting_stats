import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.vegasinsider.com/nhl/matchups/')
result = result.content
soup = BeautifulSoup(result, features="html.parser")
teams = soup.find_all('a', class_=["tableText"])
data = soup.find_all('td', class_=["viCellBg2 cellBorderL1 cellTextNorm padCenter"])

lista_equipos=[]
lista_lineas_iniciales=[]
lista_lineas_corrientes=[]

for i in teams:
    lista_equipos.append(i.text.strip())
"""The find all function returns all queries from the html...in a list of current matchups for the day and the values that we want ( opening and current lines are in the 1 and 3 position on the list (The current list len is 12 ) )"""

""" 1 3 13 15 25 27 """
#for i in range(len(data)):

opening = 1
current = 3
while (current < len(data) - 6):
    lista_lineas_iniciales.append(opening)
    lista_lineas_corrientes.append(current)
    opening = current + 10
    current = opening + 2

#print(lista_lineas_iniciales)
#print(lista_lineas_corrientes)
