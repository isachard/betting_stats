from tabulate import tabulate
from model import Data


# '25-7', 'SF', '1-0', '\u2713'],
#                    ['Maria', 90, 'Lose', '\u2717']]


"""def tabulation():
    # print(tabulate([['ARI', 'W3', 'U4', '\u2713']], [headers=['Teams', 'Streak: W/L',  'Streak: O/U', 'LastUpdate']))
    print(tabulate([['ARI', 'W3 - 53.5 %', 'L3 - 39.4%', '\u2714'],
                    ['LAD', 'L2 - 43.5 %', 'W7 - 59.1%', '\u2716']],
                   headers=[
        'Teams', 'S: W/L -> %',  'S: O/U -> %', 'LastUpdate']))
"""

"""print()
tabulation()
print()"""


def show_trends(list):
    print("We have: %i trends todays on baseball" % len(list))
    # for item in list:
    #    print item.name()


def startView():
    print("Betting Stats Application for Trends")


def endView():
    print('Goodbye!')
