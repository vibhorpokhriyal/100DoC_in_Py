# Day 1 - 3 - 001
# Learning datetime and date

from datetime import datetime
from datetime import date

print(datetime.today())

today = datetime.today()
print(type(today))         # this is a datetime object

todaydate = date.today()
print(type(todaydate))     # this is a date object

# Note - You need to keep in mind the different datetime object type
# different object types cannot be interchanged.

# calling the attributes
print(todaydate.day)
print(todaydate.month)
print(todaydate.year)

diwali = date(2023, 11, 12)
print(diwali)
print(type(diwali - date.today())) # this is a timedelta datatype. 
print((diwali - date.today()).days) # this gives us the day part only

if diwali != date.today():
    print(f"There are {(diwali - date.today()).days} to Diwali.")
else:
    print("Yay! Today is diwali.")