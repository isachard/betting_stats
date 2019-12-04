import requests
import json
import csv

lista = []

def url_format():

    _url = 'https://www.sportsline.com/sportsline-web/service/v1/odds?league=nba&auth=1'
    result = requests.get(_url)
    content = result.content
    content = content.decode('utf8').replace("'",'"')
    data = json.loads(content)

    return data

def list_of_lines(data):
    away = []
    home = []
    opening =[]
    current = []
    for i in data['competitions']:
        if 'currentTotal' in i['sportsbookOdds'][0]:
            values_to_list([i['awayTeamName'],i['homeTeamName'],
                i['sportsbookOdds'][1]['openingPointSpreadHomeHandicap'],i['sportsbookOdds'][1]['currentPointSpreadHomeHandicap'],
                i['sportsbookOdds'][1]['openingTotal'], i['sportsbookOdds'][1]['currentTotal']])

def values_to_list(values):
    global lista
    lista.append([values[0],values[1],values[2],values[3],values[4],values[5]])


def csv_writer(values):
    global lista
    with open('nhl_current.csv', mode='w') as current_trends:
        nhl_writer = csv.writer(current_trends, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        nhl_writer.writerow(["Away", "Vs", "Home", "Opening_Spread_Home", "Current_Spread_Home" ,"Opening_Line","Current_Line"])
        for i in lista :
            nhl_writer.writerow([i[0],"~",i[1],i[2],i[3],i[4],i[5] ])

def main():

    json_file = url_format()
    values = list_of_lines(json_file)
    csv_writer(values)
main()
