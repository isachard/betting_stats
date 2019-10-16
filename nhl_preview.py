import requests

from bs4 import BeautifulSoup
from tabulate import tabulate

teamdb = 55



def format_url():

    _url = "http://www.vegasinsider.com/nhl/teams/team-page.cfm/team/wild"
    result = requests.get(_url)
    content = result.content
    soup = BeautifulSoup(content, features="html.parser")
    return soup

def caller():
    soup = format_url()
    lista = get_totals_team(soup)
    print(lista)

def get_totals_team(soup):
    over, under, push = 0

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

def get_streaks_team():
    matches_spread = soup.find_all('td', class_=["viCellBg1 cellBorderL1 cellTextNorm padLeft","viCellBg2 cellBorderL1 cellTextNorm padLeft"])

    for i in matches_spread:
        i = i.text.strip()
        if (len(i) > 0):
            print(i)



def overall_totals(lista_totals):
    for i in lista_total:
        break

def last_update_date(match):
    print()
    print("Last updated: " + str(last_game_update(match)), end='')


def team_name(team):
    print()
    # print(" ".join(team.split()))
    print()


# so nhl works  like with match 0 and the it goes thru they entire website.
def record(matches):
    """Compute the current season record for the team (Win/Loss)"""
    win = 0
    lose = 0
    print(matches[0].text.split())
    # print(mat)


caller()
print()
