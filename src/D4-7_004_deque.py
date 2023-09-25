# deque = (pronounced deck) (short for double ended que)
# deque are generalized stacks and queues 
# deques have much better performance than lists

# if you have to remove from both ends of the collection consider using a deque instead of a list.

# we create a list and a deque with 10000000 elements

from collections import deque
import random, time



lst = list(range(10000000))
dck = deque(range(10000000))

def insert_and_delete(ds):
    # here the _ is used by convention for throwaway variables
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)


start = time.time()
insert_and_delete(lst)
end = time.time()
# print "Took %f ms" % ((end - start) * 1000.0)
print(f"Took {(end - start)*1000} ms")

start_dck = time.time()
insert_and_delete(dck)
end_dck = time.time()
# print "Took %f ms" % ((end - start) * 1000.0)
print(f"Took {(end_dck - start_dck)} ms")


