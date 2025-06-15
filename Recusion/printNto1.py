# print numbers from N to 1

def printNto(n):
    if(n==0):
        return
    print(n)
    printNto(n-1)

n = int(input("n : "))
printNto(n)