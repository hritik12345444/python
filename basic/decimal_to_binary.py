# Convery decimal number to binary number
# Method 1. this is manual method  
n = int(input("Enter a number : "))

binary = ""
if(n == 0):
    binary += "0"
else:
    while(n > 0):
        rem = str(n % 2 )
        binary = rem + binary  # binary me phle se jo hai wo pich concanet krna hai . rem me jo aayega phle usko rakhan hai fir binary wala ko
        n = n//2



print(binary)


# this is using functiono
# method 2

num = 20
binaryNum = bin(num)[2:]
print(binaryNum)