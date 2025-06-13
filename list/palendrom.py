# WAP to check if a list contains a palindrome of elements.

my_list = [1,"abc","abc",1]
my_list2 = my_list.copy()  # copy the my_list element into my_list2
# print(my_list2)

my_list2.reverse()  # revese the my_list2
print(my_list2)
if(my_list == my_list2):
    print("Yes, palindrome")
else:
    print("Not , Palindrome")
