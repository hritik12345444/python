# Write a recursive function to print all elements in a list.

def printEle(my_list,idx):
    if(idx == len(my_list)):
        return
    print(my_list[idx] , end=" ")  # end = " " for print in horizontal
    printEle(my_list,idx+1)

my_list =  [1,2,3,4,5,"HRITIK","singh"]
printEle(my_list,0)