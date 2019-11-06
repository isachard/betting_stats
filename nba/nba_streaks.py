import requests

from bs4 import BeautifulSoup
from tabulate import tabulate

lista_over = dict()
lista_under = dict()
for x in range(0,10):
    lista_over[x] = 0
    lista_under[x] = 0

def url_loop():
     file = open("links.txt","r")
     links = file.readlines()
     file.close()
     return links

def format_url(_url):

     result = requests.get(_url)
     content = result.content
     soup = BeautifulSoup(content, features="html.parser")
     return soup


def get_streaks(soup):
    over = 0
    under = 0
    push = 0
    matches = soup.find_all('td', class_=["viCellBg1 cellBorderR1 cellTextNorm padLeft","viCellBg2 cellBorderR1 cellTextNorm padLeft"])

#how to update thsi everytime? different algorithm to pursue
    for value in range(len(matches)):
        i = matches[value].text.strip()
        if (len(i) > 0):
            previous = i[0]

            if(i[0] == 'W'):
                over+=1
                populate_over(over)
                under = 0

            if(i[0] == 'L'):
                under+=1
                populate_under(under)
                over = 0

            if(i[0] == 'P'):
                over = 0
                under = 0

def populate_over(o):
    global lista_over
    lista_over[o]+=1

def populate_under(u):
    global lista_under
    lista_under[u]+=1


def main():

     lista_links =  url_loop()
     for i in lista_links:
         values =[]
         soup = format_url(i.strip())
         values= get_streaks(soup)

main()

print(lista_over)
print(lista_under)

values = sum(lista_over.values()) + sum(lista_under.values())
print(values)
print("460")
