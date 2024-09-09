from datetime import date

def value(year: int):
    if year % 4 == 0: return date(year, 9, 12)
    return date(year, 9, 13)
