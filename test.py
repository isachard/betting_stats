import requests

from bs4 import BeautifulSoup
from tabulate import tabulate

teamdb = 55
urlM = "https://www.covers.com/pageLoader/pageLoader.aspx?page=/data/mlb/teams/pastresults/2019/team29"
url = "https://www.covers.com/pageLoader/pageLoader.aspx?page=/data/mlb/teams/pastresults/2019/team2955.html"
result = requests.get(url)
content = result.content
soup = BeautifulSoup(content, features="html.parser")

matches = soup.find_all('tr')

team = soup.find('h1').text


def urlHandler():
    global urlM
    for teams in range(30):
        print(urlM + str(teams+teamdb))
        result = requests.get(url)
        content = result.content
        soup = BeautifulSoup(content, features="html.parser")
        matches = soup.find_all('tr')
        team = soup.find('h1').text

        team_name()


def team_name():
    print()
    print(" ".join(team.split()))
    print()


def record():
    """Compute the current season record for the team (Win/Loss)"""
    win = 0
    lose = 0

    for games in matches:
        # print(" ".join(games.text.split()))
        location = len(games.text.split())

        if (location == 16):  # away
            result = games.text.split()[3]
            if (result == 'W'):
                win += 1
            if (result == 'L'):
                lose += 1

        if (location == 15):  # home
            result = games.text.split()[2]
            if (result == 'W'):
                win += 1
            if (result == 'L'):
                lose += 1
    print("Record:")
    print(str(win) + " - " + str(lose))

    total = win + lose
    print(str("%.2f" % ((win/total)*100)) + "% - " +
          str(("%.2f" % ((lose/total)*100))) + " %")
    print()


def total():
    """Compute the current season totals for the team (Over/Under)"""
    over = 0
    under = 0

    for games in matches:
        # print(" ".join(games.text.split()))
        location = len(games.text.split())

        if (location == 16):  # away
            result = games.text.split()[13]
            if (result == 'O'):
                over += 1
            if (result == 'U'):
                under += 1

        if (location == 15):  # home
            result = games.text.split()[12]
            if (result == 'O'):
                over += 1
            if (result == 'U'):
                under += 1

    print("Totals:")
    print(str(over) + " - " + str(under))

    total = over + under
    print(str("%.2f" % ((over/total)*100)) + "% - " +
          str(("%.2f" % ((under/total)*100))) + " %")
    print()


def streaks_totals():
    """Compute the latest streak of totals)"""
    over = 0
    under = 0

    for games in matches:

        location = len(games.text.split())

        if (location == 16):  # away

            result = games.text.split()[13]

            if (result == 'O'):
                over += 1

            if (result == 'U'):
                under += 1

        if (location == 15):  # home

            result = games.text.split()[12]

            if (result == 'O'):
                over += 1

            if (result == 'U'):
                under += 1

        if (over > 0) & (under > 0):
            if over > under:
                print("Streaks Totals")
                print("Over: " + str(over))
            if under > over:
                print("Streaks Totals")
                print("Under: " + str(under))
            if over == under:
                print("Streaks Totals")
                print("Tied 1-1")
            break


def streaks_ml():
    """Compute the latest streak of win/loss"""
    win = 0
    loss = 0

    for games in matches:

        location = len(games.text.split())

        if (location == 16):  # away

            result = games.text.split()[11]

            if (result == 'W'):
                win += 1

            if (result == 'L'):
                loss += 1

        if (location == 15):  # home

            result = games.text.split()[10]

            if (result == 'W'):
                win += 1

            if (result == 'L'):
                loss += 1

        if (win > 0) & (loss > 0):
            if win > loss:
                print("Streaks MoneyLine")
                print("Win: " + str(win))
            if loss > win:
                print("Streaks MoneyLine")
                print("Loss: " + str(loss))
            if win == loss:
                print("Streaks MoneyLine")
                print("Tied 1-1")
            break


def tabulation():
    print(tabulate([['24', 'ARI', '5-4'], ['25-7', 'SF', '1-0'],
                    ['Maria', 90, 'Lose']], headers=['Date', 'VS', 'Score']))


def history_last_five():
    print()


urlHandler()
print()
