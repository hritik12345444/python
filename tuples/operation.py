# tuple in python

tup = () # empty tuples
print(tup)
print(type(tup))

tup1 = (1,) # single tuples
print(tup1)
print(type(tup1))

tup2 = (1,2,3,66,2) # tuple multiple element
print(tup2)

tup3 = ("Hritik", "BCA" , 33, 33.3)  # multipl data type tuples
print(tup3)

tuples = (3,5,1,5,3,66,77,44)
# tuples[0] = 33333  # we can't modify tuples element only access
print(tuples[0]) # only access not modified


tuples[0:2]   # not modifiy original tuples
slice_tuples = tuples[0:4]  # tuples also allow (-ve) indexing
print(slice_tuples)
print(tuples[-4:-1])   # negative indexing



print(tuples.index(66)) # return index of element
print(tuples.count(3)) # return count of element 3