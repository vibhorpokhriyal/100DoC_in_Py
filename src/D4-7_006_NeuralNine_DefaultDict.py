# defaultdict - datatype simillar to dictionary but with the twist that we have default key vaules.
#             - this allows us to create dictionaries without specifying keyvalues.


from collections import defaultdict


my_dict = defaultdict(int)

# defaultdict of class int
print(my_dict)

# the next two lines of code would error out with a dictionary
# but defaultdict assigns default values to them
print(my_dict['age'])

my_dict['some other value'] += 20

print(my_dict)

#########################################

mylist = [1,2,3,4,5,6,7,8,9]

counter = defaultdict(int)

for element in mylist:
    counter[str(element)] += element

print(counter)

##########################################

# default dict to group -

words = ["apple", "banana", "carrot", "avocado", "brocoli", "orange"]

grouped_words = defaultdict(list)

for word in words:
    grouped_words[word[0]].append(word)
print(grouped_words)

#########################################
# useful example - 
# tuple list with each tuple having 2 elements - an alphabet and a number
# add the number for the matching alphabet

tuple_list = [('A', 10), ('B', 4), ('A', 5), ('C', 7), ('B', 1)]

grouped_tup = defaultdict(list)

for key, value in tuple_list:
    grouped_tup[key].append(value)

print(grouped_tup)

grouped_tup = {k: sum(v) for k, v in grouped_tup.items()}

print(grouped_tup)
