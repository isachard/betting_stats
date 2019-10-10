import requests

from bs4 import BeautifulSoup
from tabulate import tabulate

teamdb = 55

url = "https://www.covers.com/pageLoader/pageLoader.aspx?page=/data/nba/teams/pastresults/2018-2019/team404029.html"
#result = requests.get(url)
#content = result.content
#soup = BeautifulSoup(content, features="html.parser")

#matches = soup.find_all('tr')
#team = soup.find('h1').text


def format_url(_url):
    result = requests.get(_url)
    content = result.content
    soup = BeautifulSoup(content, features="html.parser")
    matches = soup.find_all('tr')

    last_update_date(matches)

    team = soup.find('h1').text

    team_name(team)
    record(matches)
    total(matches)
    # streaks_ml(matches)
    # streaks_totals(matches)


def last_game_update(match):
    return match[1].text.split()[0]


def last_update_date(match):
    print()
    print("Last updated: " + str(last_game_update(match)), end='')


def team_name(team):
    print()
    print(" ".join(team.split()))
    print()


def record(matches):
    """Compute the current season record for the team (Win/Loss)"""
    win = 0
    lose = 0

    for games in matches:
        # print(" ".join(games.text.split()))
        location = len(games.text.split())

        games = games.text.split()

        # print(games[::-1])
        win = win + 1
        print(win)
        print(games[::-1][3])

    print("Record:")
    print(str(win) + " - " + str(lose))

    total = win + lose


def total(matches):
    """Compute the current season totals for the team (Over/Under)"""
    over = 0
    under = 0


format_url(url)

print()
