import requests

from bs4 import BeautifulSoup
from tabulate import tabulate

teamdb = 55
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


def tabulation(values):
    global teams_nhl
    headers = ["Teams", "Overall-Record", "Over", "Under"]
    table = []
    for i in range(len(teams_nhl)):
        break
        #table.append([teams_nhl[i], '0', values[i], values[i])

    print(tabulate(table,headers))
def perc_totals(values):
    total_games=values[0] + values [1] 
    over = round(values[0]/total_games * 100 ,2 )
    under = round(values[1]/total_games * 100 , 2)
    print("Over  % " + str(over))
    print("Under % " + str(under))
    print()

def main():
    global teams_nhl
    j = 0
    lista_links =  url_loop()
    for i in lista_links:
        #j = 1 + j
        values =[]
        soup = format_url(i.strip())
        values= get_totals_teams(soup)
        print(teams_nhl[j])
        perc_totals(values)
        #tabulation(values)

        j = 1 + j


main()

