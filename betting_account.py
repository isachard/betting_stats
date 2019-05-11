# Betting Accounts Stats
# Isachard Rodriguez
import datetime
from calendar import monthrange


def breakdown_weekly():
    start = 112
    now = datetime.datetime.now()
    now = int(now.strftime("%j"))

    dates_differences = now - start

    #avg_weekly = ("%.2f" % (dates_differences / 7))

    return float(dates_differences)


def breakdown_monthly():
    start = 117
    now = datetime.datetime.now()
    now = int(now.strftime("%j"))

    dates_differences = now - start

    avg_monthly = ("%.2f" % (dates_differences / 30))
    # print(avg_monthly)

    return float(avg_monthly)


def print_accounts():

    a = ((float(uSavings) - savings) / savings) * 100
    b = ((float(uBetonline) - betonline) / betonline) * 100
    c = ((float(uBookmaker) - bookmaker) / bookmaker) * 100
    d = ((float(uStoic) - stoic) / stoic)*100
    print("Nitrogen:   " + str("%.2f" % a) + "%")
    print("Betonline:  " + str("%.2f" % b) + "%")
    print("Bookmaker:  " + str("%.2f" % c) + "%")
    print("Stoic:      " + str("%.2f" % d) + "%\n")


savings = 400
bookmaker = 460
betonline = 300
stoic = 440
uSavings = 543
uBookmaker = 305.17
uBetonline = 444.06
uStoic = 493.25
start = savings + bookmaker + betonline + stoic
now = uSavings + uBookmaker + uBetonline + uStoic
print("\nBetting System Stats:")
print("Initial amount: " + str("%.2f" % start))
print("Current amount: " + str("%.2f" % now))
print()
formulaSavings = ((float(now)-start) / start) * 100
weekly_rate = formulaSavings / breakdown_weekly()
monthly_rate = formulaSavings * breakdown_monthly()
print("\nSavings up by: " + str("%.2f" % formulaSavings) + "% \n")
#print("Weekly rate by: " + str("%.2f" % weekly_rate) + "% \n")
#print("\nMonthly rate by: " + str("%.2f" %monthly_rate) + "% \n"  )
print_accounts()
#week = breakdown_weekly()
#print("Weekly rate: " + str(weekly_rate) + "%\n")
