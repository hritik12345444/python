# List in pyton almost same as array in cpp and c

#list can store multiple data type in one list

List = ["Hritk" , 37 , "Masadhi" , "College of commerce"]
print(List)
print(List[0])

# we can update/modified list 

List[0] = 44
print(List)

# list can we slice same as string
print(List[1:3])
print(List[-3:-1])
List.append(4) #append at the end of list
print(List)


list_2 = [22,52,25,0,1]
print("list 2",list_2)
# list_2.sort()   # sort in ascending order
# print(list_2)

# list_2.sort(reverse=True)  # sort in descending order
# print(list_2)

# list_2.reverse()
# print(list_2)

list_2.insert(0,999) #insert at idx 0 to the value is 999
print(list_2)

list_2.remove(22) # remove the first occurence of 22
print(list_2)

list_2.pop(2)  # remove the element at the idx 2
print(list_2)