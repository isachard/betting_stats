# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 01:09:04 2020

@author: shka
"""

import requests

from datetime import datetime
from bs4 import BeautifulSoup

import csv


teams_nhl = []
lista = []
def url_loop():
    file = open("nba_links.txt","r")
    links = file.readlines()
    file.close()
    return links

def format_url(_url):
    global teams_nhl
    #put this in a function!
    teams_nhl.append( _url[58].upper() + _url[59:])

    result = requests.get(_url)
    content = result.content
    soup = BeautifulSoup(content, features="html.parser")
    return soup

def get_totals_streaks(soup):
    lista=[]
    over = 0
    under = 0

    matches = soup.find_all('td', class_=["viCellBg1 cellBorderR1 cellTextNorm padLeft","viCellBg2 cellBorderR1 cellTextNorm padLeft"])
    for i in range(len(matches)):
        matches[i] = matches[i].text.strip()
        if (len(matches[i]) > 0): 
            lista.append(matches[i]) 
    lista.reverse()
    for i in range(len(lista)):     
                  
        if lista[i][0] == 'U':
            under = under + 1
            if lista[i+1][0] != 'U':
                return "Under: " +str(under)
            
        if lista[i][0] == 'O':
            over = over + 1
            
            if lista[i+1][0] != 'O':
                return "Over: " + str(over)
        

def get_totals_trends(soup):
    over = 0
    under = 0
    push = 0

    matches = soup.find_all('td', class_=["viCellBg1 cellBorderR1 cellTextNorm padLeft","viCellBg2 cellBorderR1 cellTextNorm padLeft"])
    for i in matches:
        

        i = i.text.strip()
        if (len(i) > 0):
            print(Convert(i))
            if(i[0][0] == 'W'):
                over +=1
            if(i[0][0] == 'L'):
                under +=1
            if(i[0][0] == 'P'):
                push += 1

    return [over,under,push]

def csv_writer():
    global lista
    with open('nba_current.csv', mode='w') as current_trends:

        nhl_writer = csv.writer(current_trends, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        nhl_writer.writerow(["Teams", "Over", "Under", "Push","Over %", "Under %", "Streaks"])
        for item in lista :
            total = item[1] + item[2]
            over = round((item[1] / total) * 100,1)
            under = round((item[2] / total) * 100,1)
            nhl_writer.writerow([item[0],item[1],item[2],item[3],over,under, item[4]])

def team_values_to_list(team,trends,streaks):
    global lista
    lista.append([team[-1:], trends[0],trends[1],trends[2],streaks])
    print(team[-1:])
    
    
def Convert(string): 
    li = list(string.replace("\t", "").replace("\r", "").replace("\n", "").replace("\xa0", "").replace("/", "")
    .split(" ")) 
    return li 

def main():
    global teams_nhl
    j = 0
    lista_links =  url_loop()
    for i in lista_links:
        values =[]
        soup = format_url(i.strip())
        trends_values= get_totals_trends(soup)
        streaks_values = get_totals_streaks(soup)
        team_values_to_list(teams_nhl, trends_values, streaks_values)
    csv_writer()



main()