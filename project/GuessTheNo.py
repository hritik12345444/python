# Mini Project
# Guesse the number  

import random

ran = random.randint(1,1000)  # both are included
# print(ran)

itr = True
while(itr == True):  # loop lagaye hai taki jabb tkk input sahi na de tbb tkk bar bar game aage chalte rhega
    target = input("Guesse the number (Quit): ") # target me abhi string hai 
    if(target == "Quit"):
        print("you Quit the game")
        print("____Game Over____")
        break
    target = int(target)  # target ko integer me convert krr diye 
    if(target == ran):
        print("Congrulations  Target found 😊😊..")
        print("______Game Over______")
        itr = False
    elif(target < ran):
        print("Choose a bigger no🤦🤦...")
    else:
        print("Choose a smaller no🤦🤦...")