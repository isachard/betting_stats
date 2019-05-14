import requests

from bs4 import BeautifulSoup
from tabulate import tabulate


url = "https://www.covers.com/pageLoader/pageLoader.aspx?page=/data/mlb/teams/pastresults/2019/team2957.html"
result = requests.get(url)
content = result.content
soup = BeautifulSoup(content, features="html.parser")

a = soup.find_all('tr')

# print(a[1])
# print(a[7])


# print(len(a))

team_name = soup.find('h1').text
print(team_name)
#print(" ".join(team_name.split()))


def record():
    win = 0
    lose = 0

    for games in a:
        #print(" ".join(games.text.split()))
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


def total():
    over = 0
    under = 0

    for games in a:
        #print(" ".join(games.text.split()))
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


def streaks_totals():
    over = 0
    under = 0
    for games in a :
        
        location = len(games.text.split())

        if (location == 16):  # away
            result = games.text.split()[13]
            if (result == 'O'):
                over += 1
                under = 0
            if (result == 'U'):
                under += 1
                over = 0

        if (location == 15):  # home
            result = games.text.split()[12]
            if (result == 'O'):
                over += 1
                under = 0
            if (result == 'U'):
                under += 1
                over = 0
    print("Streaks Total:")
    print(str(over) + " - " + str(under))


def streaks_ml():
    win = 0
    lose = 0
    
    for games in a :
        
        location = len(games.text.split())

        if (location == 16):  # away
            #print(games.text.split()[11])
            result = games.text.split()[11]
            if (result == 'W'):
                win += 1
                lose = 0
            if (result == 'L'):
                lose += 1
                win = 0

        if (location == 15):  # home
            #print(games.text.split()[10])
            result = games.text.split()[10]
            if (result == 'W'):
                win += 1
                lose = 0
            if (result == 'L'):
                lose += 1
                win = 0
    print("Streaks MoneyLine")
    print( str(win) + " - " + str(lose))



# def team_history():
def tabulation():
    print(tabulate([['24', 'ARI', '5-4'], ['25-7', 'SF', '1-0'],
                ['Maria', 90, 'Lose']], headers=['Date', 'VS', 'Score']))
record()
total()
streaks_totals()
streaks_ml()
