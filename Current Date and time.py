
from datetime import date, time, datetime

today = date.today()
now = datetime.now()
print("Today's date is",today)
print("\nCurrent date and time is ", now)

print("\ndate components",today.year, today.month,today.day)
