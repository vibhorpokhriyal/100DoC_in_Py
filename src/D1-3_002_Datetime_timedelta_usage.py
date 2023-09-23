# Day 1 - 3 - 002
# timedelta usage
# timedelta can be thought of as a static amount of time. You can add / subtract it to other time objects.

from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)
print(type(t))
print(t)

print(t.days)
# note that the seconds here is not for the number of days. Seconds part cannot exceed 24 hours.
# the seconds here is for the hours part i.e., 10
print(t.seconds)

print(t.seconds/60/60) # 10 hours

# t.hours # this will error out. there is no hours attribute

eta = timedelta(hours=6)

today = datetime.today()
print(today)
# see that it gives to a datetime object just 6 hours in the future
print(today + eta)