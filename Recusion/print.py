# print number from 1 to n

def printNU(n):
    if(n == 0):
        return
    printNU(n-1)
    print(n)

n = int(input("n : "))
printNU(n)