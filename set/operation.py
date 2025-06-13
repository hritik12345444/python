# set in python

# set store multiple unique items in single variable
# sets are unordered
# do not allow duplicate values
# jo immutable hote hai whi set me store ho skte hai
# set ignore the duplicate value

# initialization of set

my_set = {1,2,3,4} # 1 notmally intitialization
# print(type(my_set))
# print(my_set)

my_set2 = set([1,2,3,4,])# 2  through set function
# print(my_set2)
# print(type(my_set2))

# we can initialize null set using set function
null_set = set() # null set this is nothing store now 
# print(null_set)
# print(type(null_set))

new_set = {1,3,4,5,"hello" , "world"}
new_set.add(11) # this will add an element at anywhere in set because set in unorder data structure
new_set.add("tsunami")
print(new_set)

new_set.remove(1)  # this will be remove the element from set
print(new_set)

my_set.clear() # this will delet everything in set clear the set
print(my_set)  # print empty set

new_set.pop() # this will delet any element from set 
print(new_set)
print(type(new_set))