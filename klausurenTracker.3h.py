#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from datetime import date

# add your events and deadlines into the dictionary
klausuren = {
    "exam 1": date(2019, 9, 24),
    "exam 2": date(2019, 12, 31)
}
daysList = {}
today = date.today()


# calculate empty spaces for printing
def empty(klausur):
    fehlt = 10 - len(klausur)
    if fehlt > 0:
        return " " * fehlt


# get days until Klausur
for klausur, date in sorted(klausuren.items()):
    delta = date - today
    days = delta.days
    daysList[days] = klausur

nextKlausur = min(daysList.keys())

# show next Klausur in menubar
if nextKlausur > 0:
    if nextKlausur > 7:
        weeks = nextKlausur // 7
        restDays = nextKlausur % 7
        print(str("📚" + daysList.get(nextKlausur)) + " " + str(weeks) + "W, " + str(restDays) + "T")
    else:
        print(str("📚" + daysList.get(nextKlausur)) + " " + str(nextKlausur) + "T")
print("---")

# print data
for klausur, date in sorted(klausuren.items()):
    delta = date - today
    days = delta.days

    if days > 0:
        if days > 7:
            weeks = days // 7
            restDays = days % 7
            print(klausur + ":" + empty(klausur) + "noch " + (
                str(weeks) if weeks > 9 else "0" + str(weeks)) + " Wochen, " + str(restDays) + (" Tage " if restDays > 1 else " Tag  ") + "(" + str(
                date) + ") | font=Menlo size=14") # color=white

        else:
            print(klausur + ": noch " + str(days) + " Tage (" + str(date) + ")")