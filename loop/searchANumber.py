# 5. Search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100)

my_tuple = (1,4,9,16,25,36,49,64,81,100,1)
i = 0
x = int(input("number : "))
found = False
while(i < len(my_tuple)):
    if(my_tuple[i] == x):
        print(f"Yes present at index {i} and the value is {x} ")  # in this line we write her f for formate string iski wahjah se hmm string ke bich me run time value insert krr skte hai
        found = True
        break
    else:
        print("Searching....")
    i+=1
if(found != True):
    print("Sorry, Data is not found ......")
   