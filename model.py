import json


class Data(object):

    def __init__(self):

    @classmethod
    def start_engine(self):

        teamdb = 55
        urlM = "https://www.covers.com/pageLoader/pageLoader.aspx?page=/data/mlb/teams/pastresults/2019/team29"
        url = "https://www.covers.com/pageLoader/pageLoader.aspx?page=/data/mlb/teams/pastresults/2019/team2955.html"

        for teams in range(30):
            _url = urlM + str(teams+teamdb) + ".html"
            result = requests.get(_url)
            content = result.content
            matches = BeautifulSoup(
                content, features="html.parser").find_all('tr')

        return matches

        # process done

        last_update_date(matches)

        team_name(team)
        record(matches)
        total(matches)
        streaks_ml(matches)
        streaks_totals(matches)


"""
        database = open('db.txt', 'r')
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            item = json.loads(item)
            data = data(item['first_name'], item['last_name'])
            result.append(data)
        return result"""
