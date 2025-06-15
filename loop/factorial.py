# WAP to find the factorial of first n numbers. (using for)

n = int(input("n : "))
fact = 1

for i in range(1,n+1,1):   # starting point 1 , ending point n+1, incremenent by one step
    fact *= i
print(fact)