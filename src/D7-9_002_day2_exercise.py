
cars = {
    "Ford":["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan":["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"]
}

# get all the jeeps
for k, v in cars.items():
    if k == "Jeep":
        for e in v:
            print(e)

print("-----------------------------")

# Get the first car of each manufacturer

for k, v in cars.items():
    print(v[0])

print("-----------------------------")

# Get all vehicles containing the string 'Trail' in its name (should work for other grep too)

for k, v in cars.items():
    for e in v:
        if e.upper().find("TRAIL") != -1:
            print(e)

print("-----------------------------")

# Sort the models values alphabetically
temp_list = []

for value_list in cars.values():
    for value in value_list:
        temp_list.append(value)

temp_list.sort()
for model_name in temp_list:
    print(model_name)