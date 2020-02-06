#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from datetime import date
import operator

###############Settings#####################################
# add your events and deadlines into the dictionary in the following format:
# "(Klausurname)": date((Jahr), (Monat), (Tag)),
klausuren = {
    "Mathe": date(2020, 2, 8),
    "Latein": date(2020, 6, 29),
    "Spanisch": date(2020, 2, 2),
    "Kunst": date(2020, 2, 12)
}
# add your colorscheme into the dictionary in the following format:
# (Anzahl der Tage bis zur Klausur, ab der die Farbe angezeigt werden soll): " color=(red, yellow, orange, green, oder #ff2800 hexcode)",
colors = {
    14: " color=red",
    21: " color=#ff6100",
    27: " color=yellow",
    35: " color=green"
}

# if you want to show the next Klausur in the menubar in color, set to true, for white color set false
showNextKlausurInColor = True
#############################################################

daysList = {}
today = date.today()

# convert dictionary into sorted tuple
klausuren_sorted = sorted(klausuren.items(), key=operator.itemgetter(1))


# calculate empty spaces for printing
def empty(klausur):
    fehlt = 10 - len(klausur)
    if fehlt > 0:
        return " " * fehlt


def getColorString(days):
    for time, string in colors.items():
        if days <= time:
            return string
        elif days > list(colors.keys())[-1]:
            return list(colors.values())[-1]


# get days until Klausur
for klausur, date in klausuren_sorted:
    delta = date - today
    days = delta.days
    daysList[days] = klausur


def getNextKlausur():
    for date in sorted(daysList.keys()):
        if date > 0:
            return date


nextKlausur = getNextKlausur()

# show next Klausur in menubar
if nextKlausur > 0:
    color = getColorString(nextKlausur)
    if nextKlausur > 7:
        weeks = nextKlausur // 7
        restDays = nextKlausur % 7
        print(str("📚" + daysList.get(nextKlausur)) + " " + (
            str(weeks) + "W, " + str(restDays) + "T | " + color if restDays > 0 else str(weeks) + "W" + ((" | " + color) if showNextKlausurInColor else "")))
    else:
        print(str("📚" + daysList.get(nextKlausur)) + " " + str(nextKlausur) + "T" + ((" | " + color) if showNextKlausurInColor else ""))
print("---")

# print data
for klausur, date in klausuren_sorted:
    delta = date - today
    days = delta.days
    color = getColorString(days)

    if days > 0:
        if days > 7:
            weeks = days // 7
            restDays = days % 7
            if restDays == 0:
                print(klausur + ":" + empty(klausur) + "noch " + (str(weeks) if weeks > 9 else "0" + str(weeks)) + (
                    " Wochen" if weeks > 1 else " Woche ") + "         (" + date.strftime(
                    '%d.%m.%Y') + ") | font=Menlo size=14" + color + " terminal=false bash=''")  # you can change the font, you should use a monospaced font for the best look
            else:
                print(klausur + ":" + empty(klausur) + "noch " + (str(weeks) if weeks > 9 else "0" + str(weeks)) + (
                    " Wochen, " if weeks > 1 else " Woche,  ") + str(restDays) + (
                          " Tage " if restDays > 1 else " Tag  ") + "(" + date.strftime(
                    '%d.%m.%Y') + ") | font=Menlo size=14" + color + " terminal=false bash=''")  # color=white
        else:
            print(klausur + ":" + empty(klausur) + "noch 0" + str(days) + " Tage           (" + date.strftime(
                '%d.%m.%Y') + ") | font=Menlo size=14" + color + " terminal=false bash=''")
