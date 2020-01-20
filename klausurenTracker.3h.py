#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from datetime import date
import operator

# add your events and deadlines into the dictionary
klausuren = {
    "Mathe": date(2019, 9, 12),
    "Latein": date(2019, 7, 5),
    "Spanisch": date(2019, 7, 3)
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
        weeks = days // 7
        restDays = days % 7
        tagenull = ""

        if restDays == 1:
            tagetitle = "Tag "
        elif restDays == 0:
            tagetitle = ""
            tagenull = ""
            restDays = ""
            weekcomma = "     "
        else:
            tagetitle = "Tage"

        if days > 7:
            if weeks < 10:
                weeksfiller = "0"
            else:
                weeksfiller = ""

            if days > 14:
                weektitle = "Wochen"
            else:
                weektitle = "Woche "

            weekcomma = ", "
            noweekspace = ""


        else:
            weeksfiller = ""
            weeks = ""
            weekcomma = ""
            weektitle = ""
            noweekspace = "          "

        print("{}:{}noch {}{} {}{}{}{} {} {}({}) | font=Menlo size=14 terminal=false bash=''".format(klausur, empty(klausur), weeksfiller,
                                                                                 str(weeks), weektitle, weekcomma,
                                                                                 tagenull, restDays, tagetitle, noweekspace, date))