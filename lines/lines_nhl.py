import requests
import json
import csv

def url_format():

    _url = 'https://www.sportsline.com/sportsline-web/service/v1/odds?league=nhl&auth=1'
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
            away.append(i['awayTeamName'])
            home.append(i['homeTeamName'])
            opening.append(i['sportsbookOdds'][0]['openingTotal'])
            current.append(i['sportsbookOdds'][0]['currentTotal'])
    return ([away,home] ,[opening, current])

def csv_writer(values):
    with open('nhl_current.csv', mode='w') as current_trends:
        nhl_writer = csv.writer(current_trends, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        nhl_writer.writerow(["Away", "Vs", "Home", "Opening_Line","Current_Line"])
        #print(values)
        #print(len(values))
        #print(values)
        #print(values[0])
        #print(values[1])
        for i in values :
            #nhl_writer.writerow([i[0],"~",i[1],i[2],i[3] ])
            #print(i)
            print(i[0])
            #print(i)
            #print("  ")
def main():

    json_file = url_format()
    values = list_of_lines(json_file)
    csv_writer(values)
main()
