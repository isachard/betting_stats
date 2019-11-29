import csv
import requests
from bs4 import BeautifulSoup






def handling_url():
    _url = 'https://www.vegasinsider.com/nhl/matchups/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    result = requests.get(_url, headers=headers)
    result = result.content
    soup = BeautifulSoup(result, features="html.parser")
    return soup

def extracting_data(soup):
    teams = soup.find_all('a', class_=["tableText"])
    data = soup.find_all('td', class_=["viCellBg2 cellBorderL1 cellTextNorm padCenter"])
    time = soup.find_all('td', class_=["viSubHeader1 cellBorderL1 headerTextHot padLeft"])
    equipos=[]
    tiempo = []
    lineas_iniciales=[]
    lineas_corrientes=[]

    for i in time:
        tiempo.append(i.text.strip())

    for i in range(2, len(teams), 2):

        equipos.append([teams[i].text.strip(), teams[i+1].text.strip()])



    """The find all function returns all queries from the html...in a list of current matchups for the day and the values that we want ( opening and current lines are in the 1 and 3 position on the list (The current list len is 12 ) )"""
    """ 1 3 13 15 25 27 """

    opening = 0
    while (opening < len(data) -13 ):
        if (opening == 0):
            opening = 1
            current = 3

            lineas_iniciales.append(data[opening].text.strip())
            lineas_corrientes.append(data[current].text.strip())

            opening = 15
            current = 17
        else:

            opening = current + 10
            current = opening + 2

            lineas_iniciales.append(data[opening].text.strip())
            lineas_corrientes.append(data[current].text.strip())

    #del equipos[0:2]

    return ([tiempo, equipos,lineas_iniciales,lineas_corrientes ])

def create_csv(values):
    with open('matchups.csv', mode='w') as matchups:
        matchups_writer = csv.writer(matchups, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        matchups_writer.writerow(["Time", "Away", "Home", "Opening Line",  "Current Line", "Result"])

        for i in range(len(values[0])):
            print(values[0][i])

            print(values[0][i][0])
            matchups_writer.writerow([values[0][i],values[1][i][0], values[1][i][1], values[2][i],values[3][i]])
def main():

    soup = handling_url()
    values = extracting_data (soup)
    print(values)
    create_csv(values)
main()
