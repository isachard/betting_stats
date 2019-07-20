from tabulate import tabulate

# '25-7', 'SF', '1-0', '\u2713'],
#                    ['Maria', 90, 'Lose', '\u2717']]


def tabulation():
    # print(tabulate([['ARI', 'W3', 'U4', '\u2713']], [headers=['Teams', 'Streak: W/L',  'Streak: O/U', 'LastUpdate']))
    print(tabulate([['ARI', 'W3', 'L3', '\u2714']], headers=[
          'Teams', 'S: W/L',  'S: O/U', 'LastUpdate']))


print()
tabulation()
print()
