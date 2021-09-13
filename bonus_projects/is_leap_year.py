'''
Program to check if a year is a leap year.
'''

from datetime import datetime as dt

try:
    year=int(input("Please insert a year: "))
except:
    while True:
        try:
            year=int(input("Please insert a valid year: "))
            break
        except:
            continue

isleap = True

if year % 4 != 0:
    isleap=False
else:
    if (year % 100 == 0) and (year % 400 != 0):
        isleap=False

current_year = dt.now().year
if year < current_year:
    verb = "was" if isleap else "was NOT"
elif year == current_year:
    verb = "is" if isleap else "is NOT"
else:
    verb = "will be" if isleap else "will NOT be"
 
print(f"{year} {verb} a leap year!")