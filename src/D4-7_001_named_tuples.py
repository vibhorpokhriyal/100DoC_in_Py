# collections module = this gives us specialized container datatypes providing an alternative to general purpose built-in containers like dict, list, tuple and set.

from collections import namedtuple


normal_tuple = ("Bob", "Coder")

# see that normal tuples are not very meaningful
# the order does not tell us anything 
# leading to the ugly code you see below
print(f"User {normal_tuple[0]} is a {normal_tuple[1]}")

# namedtuple(tuple_name, tuple_fields)
# tuple_fields = give as many fields as you would like seperated by a space
User = namedtuple("User", "name role")

# call the namedtuple and assign to a variable
user = User("Bob", "Coder")

# you can now just user the tuple.attribute format to use the fields
print(f"User {user.name} is a {user.role}")