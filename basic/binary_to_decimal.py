# Conver Binary to decimal


n = int(input("Enter a binary no. "))
dec_num = 0
if(n == 0):
    dec_num = 0
else:
    i = 0
    while(n > 0):
        rem = n % 10
        dec_num += rem * 2 ** i
        i+=1
        n = n//10

print(f"your decimal number is {dec_num}")
