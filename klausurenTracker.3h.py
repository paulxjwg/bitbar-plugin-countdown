#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from datetime import date
import operator

# add your events and deadlines into the dictionary
klausuren = {
    "Mathe": date(2019, 9, 12),
    "Latein": date(2019, 12, 31),
    "Spanisch": date(2019, 9, 2)
}
daysList = {}
today = date.today()

# convert dictionary into sorted tuple
klausuren_sorted = sorted(klausuren.items(), key=operator.itemgetter(1))


# calculate empty spaces for printing
def empty(klausur):
    fehlt = 10 - len(klausur)
    if fehlt > 0:
        return " " * fehlt


# get days until Klausur
for klausur, date in klausuren_sorted:
    delta = date - today
    days = delta.days
    daysList[days] = klausur
nextKlausur = min(daysList.keys())

# show next Klausur in menubar
if nextKlausur > 0:
    if nextKlausur > 7:
        weeks = nextKlausur // 7
        restDays = nextKlausur % 7
        print(str("📚" + daysList.get(nextKlausur)) + " " + (
            str(weeks) + "W, " + str(restDays) + "T" if restDays > 0 else str(weeks) + "W"))
    else:
        print(str("📚" + daysList.get(nextKlausur)) + " " + str(nextKlausur) + "T")
print("---")

# print data
for klausur, date in klausuren_sorted:
    delta = date - today
    days = delta.days

    if days > 0:
        if days > 7:
            weeks = days // 7
            restDays = days % 7
            if restDays == 0:
                print(klausur + ":" + empty(klausur) + "noch " + (
                    str(weeks) if weeks > 9 else "0" + str(weeks)) + " Wochen         (" + str(
                    date) + ") | font=Menlo size=14") # you can change the font, you should use a monospaced font for best results
            else:
                print(klausur + ":" + empty(klausur) + "noch " + (
                    str(weeks) if weeks > 9 else "0" + str(weeks)) + " Wochen, " + str(restDays) + (
                          " Tage " if restDays > 1 else " Tag  ") + "(" + str(
                    date) + ") | font=Menlo size=14")
        else:
            print(klausur + ":" + empty(klausur) + "noch 0" + str(days) + " Tage           (" + str(
                date) + ") | font=Menlo size=14") # color=white
