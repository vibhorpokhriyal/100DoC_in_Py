# Bro Code - 019 - Countdown Timer

import time

# you can use the sleep function to sleep for a given amont of time
#  time.sleep(3)
# print("TIMES UP!")

my_time = int(input("Enter time in seconds: "))

# for x in range(0, my_time):
#     print(x)
#     time.sleep(1)

# to reverse the countdown we can reverse the range and add a step of -1
for x in range(my_time, 0, -1):
    # we are using % (modulus) to get the remainder here
    # we divide by 60 because there are 60 seconds in a minute i.e., seconds cannot exceed 60
    # so if x > 60 you get the remainder and if x < 60 you get x itself as remainder.
    # thus making sure that the seconds counter runs between 0 and 60
    seconds = x % 60
    # remember that the user is entering time in seconds.
    # so to convert seconds to minutes we divide by 60.
    # the purpose of modulus 60 is same as seconds section.
    minutes = int((x/60)%60)
    # there are 3600 seconds in an hour.
    # note that we are not using the % (modulus) operator here because we don't plan to use a day part in our counter
    # seconds and minutes have the modulus operator to ensure that those parts only run between 0-60
    # if we do plan to use a day part. hours will be divided by 24 i.e., hours % 24
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIMES UP!")