import requests

from bs4 import BeautifulSoup
from tabulate import tabulate

teamdb = 55

url = "http://www.vegasinsider.com/nhl/teams/team-page.cfm/team/bruins"


def format_url(_url):
    result = requests.get(_url)
    content = result.content
    soup = BeautifulSoup(content, features="html.parser")
    matches = soup.find_all('td')

    for i in matches:
        print(i.text.strip())

    # first call
    # last_update_date(matches)
    #team = soup.find('h1').text

    # record(matches)


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


format_url(url)
print()
