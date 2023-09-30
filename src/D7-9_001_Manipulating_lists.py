
numlist = [1,2,3,4,5]

print(numlist)

# you can reverse a list
numlist.reverse()

print(numlist)

# you can sort a list
numlist.sort()

print(numlist)

# a simple but powerful code
# very frequently used in python 
for num in numlist:
    print(str(num))

###########################

mystring = "julian"

# converts to a list
# each letter is a string
l = list(mystring)

print(l)

# index

print(l[0])
print(l[2])

# .pop() = returns the last element from the list and removes it from the list in the process

print(l.pop())
print(l)

# .insert(index, element) = adds element to a list at the position provided.

l.insert(5, "n")
print(l)

# replacing an element from a list
l[0] = "b"

print(l)

# delete an element from the list (unlike a pop, del does not return anything)
del l[0]

print(l)

l.insert(0, "m")

print(l)

# pop(index) - pop value at specific index
l.pop(0)

print(l)

# adding element to the last position

l.append("s")

print(l)
