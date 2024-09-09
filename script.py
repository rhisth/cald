from sys import argv, exit
from datetime import date
from cald import getday, getdays

if len(argv) != 3: exit()
try:
    year = int(argv[2])
    if argv[1] == "all": days = getdays(year)
    elif argv[1] == "today":
        date = date.today().replace(year=year)
        days = [day for day in getdays(year) if day[1] == date]
    else: days = (getday(argv[1], year))
    for day in days:
        print(day[0], day[1], sep="\n")
except Exception as ex: print(ex)