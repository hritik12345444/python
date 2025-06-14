# print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
my_list = [1,4,9,16,25,36,49,64,81,100]
# syntax of for loop

for ele in my_list:
    print(ele)
else:
    print("Work done!.....")





# Search for a number x in this tuple using loop:
my_tuple = (1,4,9,16,25,36,49,64,81,100)

for ele in my_tuple:
    print(ele)
else:
    print("Work done!...")




# Print numbers from 100 to 1
# for loop with range 100 is start , 0 is stop and -1 is decrement/increment
for i in range (100,0,-1):
    print(i)






# Print numbers from 1 to 100
for i in range(1,101,1):
    print(i)





# Print the multiplication table of a number n.
num = int(input("num : "))
for i in range(1,11,1): # starting point 0 ending point 11 but 11 not include step for increment q by defalut stating point 0 hi hota hai
    print(num,"*",i,"=",num*i)