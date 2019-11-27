import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.vegasinsider.com/nba/matchups/')
result = result.content
soup = BeautifulSoup(result, features="html.parser")
teams = soup.find_all('a', class_=["tableText"])
data = soup.find_all('td', class_=["viCellBg2 cellBorderL1 cellTextNorm padCenter"])

print(teams, data)

