import requests

from datetime import datetime
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv


teams_nhl = []
def url_loop():
    file = open("links.txt","r")
    links = file.readlines()
    file.close()
    return links

def format_url(_url):
    global teams_nhl
    #put this in a function!
    teams_nhl.append( _url[57].upper() + _url[58:])

    result = requests.get(_url)
    content = result.content
    soup = BeautifulSoup(content, features="html.parser")
    return soup

def caller():
    soup = format_url()
    lista = get_totals_team(soup)
    print(lista)

def get_totals_teams(soup):
    over = 0
    under = 0
    push = 0

    matches = soup.find_all('td', class_=["viCellBg1 cellBorderR1 cellTextNorm padLeft","viCellBg2 cellBorderR1 cellTextNorm padLeft"])
    for i in matches:

        i = i.text.strip()
        if (len(i) > 0):
            if(i[0] == 'O'):
                over +=1
            if(i[0] == 'U'):
                under +=1
            if(i[0] == 'P'):
                push += 1

    return [over,under,push]

def csv_writer(values, team):
    today = datetime.today()
    today_number = today.day

    reader = csv.reader(f)
    row1 = next(reader)
    if (today_number != row1 )

        with open('nhl_current.csv', mode='a') as current_trends:
            nhl_writer = csv.writer(current_trends, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            nhl_writer.writerow([team,values[0],values[1],values[2]])



def main():
    global teams_nhl
    j = 0
    lista_links =  url_loop()
    for i in lista_links:
        values =[]
        soup = format_url(i.strip())
        values= get_totals_teams(soup)
        csv_writer(values, teams_nhl[j])

        j = 1 + j


main()

