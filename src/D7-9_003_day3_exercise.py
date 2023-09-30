import D7_9_003_data

# print(D7_9_003_data.us_state_abbrev)

# print 10th item in each
print(D7_9_003_data.states_list[9])

x = 0
for k, v in D7_9_003_data.us_state_abbrev.items():
    x += 1
    if x == 10:
        print(f"key: {k} : value: {v}")
    

print("--------------------------------")

# Print 45th key in dictionary

us_state_abbrev_keys = list(D7_9_003_data.us_state_abbrev.keys())

# print(us_state_abbrev_keys)

for element in us_state_abbrev_keys:
    if element == D7_9_003_data.states_list[44]:
        print(element)

print("--------------------------------")

# Print out the 27th value in the dictionary.

print(D7_9_003_data.us_state_abbrev.get(D7_9_003_data.states_list[26]))