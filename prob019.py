def daysinmonth(month, year):
    if month in (0, 2, 4, 6, 7, 9, 11):
        return 31
    if month in (3, 5, 8, 10):
        return 30
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 29
    else:
        return 28

daysinmonths = {}

for y in range(1900, 2001):
    daysinmonths[y] = [daysinmonth(m, y) for m in range(12)]

daycount = 1

sundaycount = 0

for y in range(1901, 2001):
    for d, days in enumerate(daysinmonths[y]):
        if daycount % 7 == 0:
            sundaycount += 1
            print(y, d, days)
        daycount += days
        
print(sundaycount)