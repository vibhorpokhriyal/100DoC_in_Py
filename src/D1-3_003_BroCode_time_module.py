# Bro Code - 067 - time module

import time

# epoch = when your computer thinks time began (reference point)
print(time.ctime(0)) # convert a time expressed in seconds since epoch to a readable string

print(time.ctime(1000000)) # 1 million seconds since epoch

print(time.time()) # returns current seconds since epoch

# current time

print(time.ctime(time.time()))

time_object = time.localtime()
# time.gmtime() = to get the UTC time
print(time_object)

# time.strftime(format, timeobject) = str: string + f: format + time
# https://docs.python.org/3/library/time.html

localtime = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(localtime)

# time.strptime(time_in_string, format)
# takes string representation of time and format and returns a time object

time_string = "20 April, 2023"
time_object_2 = time.strptime(time_string, "%d %B, %Y") # notice that the format exactly matches the time string you have provided 
print(time_object_2)

# time tuple
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string_2 = time.asctime(time_tuple) # returns a string that is in ascii format
mk_time_string = time.mktime(time_tuple) # takes time tuple and returns seconds since epoch
print(time_string_2)
print(mk_time_string)