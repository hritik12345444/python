# WAF to print the elements of a list in a single line. (list is the parameterr)

def my_list (list):
    for i in list :
        print(i , end = " ")   # if we don't write end = " " , than print in vertically in terminal 

my_list1 = [1,2,3,4,5,6,7]
my_list(my_list1)