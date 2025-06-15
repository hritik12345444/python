# WAF (write a function) to print length of a list. (list is the paameter)

# defining a function

def lenOfList(list_name):
    return len(list_name)


my_list = [1,3,4,5,6,"hello",6]
length = lenOfList(my_list)
print(length)