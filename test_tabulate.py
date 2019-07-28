from tabulate import tabulate


# '25-7', 'SF', '1-0', '\u2713'],
#                    ['Maria', 90, 'Lose', '\u2717']]

def tabulation():
    # print(tabulate([['ARI', 'W3', 'U4', '\u2713']], [headers=['Teams', 'Streak: W/L',  'Streak: O/U', 'LastUpdate']))
    print(tabulate([['ARI', 'W3 - 53.5 %', 'L3 - 39.4%', '\u2714'], ['VS'],
                    ['LAD', 'L2 - 43.5 %', 'W7 - 59.1%', '\u2716']],
                   headers=[
        'Teams:', 'Streaks: W/L',  'Streaks: O/U', 'Last Update']))


print()
tabulation()
print()
