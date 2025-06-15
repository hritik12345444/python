# WAP to find the factorial of first n numbers. (using for)

n = int(input("n : "))
fact = 1

# find fact of n
# for i in range(1,n+1,1):   # starting point 1 , ending point n+1, incremenent by one step
#     fact *= i
# print(fact)


# find fact of n numbers starting from 1 to n 
# this is nested loop
for i in range(1,n+1,1):    # outer loop
    fact = 1
    for j in range(1,i+1,1): # inner loop  j start from 1 end at i+1 incremenent by 1 step
        fact *= j
    print( f"fact of {i} is :-> ",fact)
