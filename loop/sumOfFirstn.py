# WAP to find the sum of first n numbers. (Using while)

i = 1
n = int(input("n : "))
sum = 0
while(i <= n):
    sum += i
    i+=1  # incrementation step
print("Sum of first n natural number is : ",sum)