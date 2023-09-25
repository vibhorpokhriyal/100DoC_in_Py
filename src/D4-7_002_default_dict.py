from collections import defaultdict

users = {"bob": "coder"}

print(users["bob"])

# if key not in dictionary you get a KeyError
try:
    print(users["julian"])
except KeyError as e:
    print(e)

print(users.get("bob"))

print(users.get("julian")) # if key not in dictionary returns None (does not result in an error and stop the program)

# note that the list of tuples repeats the names
# we will try to make a dictionary for this
challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]
# becuase there are repeating key names we will get a key error with a normal dictionary
try:
    challenges = {}
    for name, challenge in challenges_done:
        challenges[name].append(challenge)
except Exception as e:
    print(f"Error {type(e).__name__} for {e}")

# using default dict

# you need to tell the defaultdict function what kind of values will it hold
# here it will be holding a list 
# for a single key there will be a list of values
challenges = defaultdict(list)

for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)