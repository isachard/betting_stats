import requests

from bs4 import BeautifulSoup
from tabulate import tabulate

teamdb = 55

def url_loop():
    file = open("links.txt","r")
    links = file.readlines()
    file.close()
    return links

def format_url(_url):

    #put this in a function!
    team_name = _url[57].upper() + _url[58:]
    print(team_name)
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
            if(i[0] == 'W'):
                over +=1
            if(i[0] == 'L'):
                under +=1
            if(i[0] == 'P'):
                push += 1

    return [over,under,push]

def get_streaks_teams():
    matches_spread = soup.find_all('td', class_=["viCellBg1 cellBorderL1 cellTextNorm padLeft","viCellBg2 cellBorderL1 cellTextNorm padLeft"])

    for i in matches_spread:
        i = i.text.strip()
        if (len(i) > 0):
            print(i)

def get_last_streaks():
    matches = soup.find_all('td', class_=["viCellBg1 cellBorderR1 cellTextNorm padLeft","viCellBg2 cellBorderR1        cellTextNorm padLeft"])
    for i in matches:
        i = i.text.strip()
        break

def perc_totals(values):

    total_games=values[0] + values [1] + values [2]
    
    over = values[0]/total_games   
    under =values[1]/total_games  
    print("Over  % " + str(over))
    print("Under % " + str(under))
    print(str(values[0]) + "   -   "  +str(values[1]) ) 
    print()

def main():

    lista_links =  url_loop()
    for i in lista_links:
        values =[]
        soup = format_url(i.strip())
        print(values)
        values= get_totals_teams(soup)
        perc_totals(values)




main()

