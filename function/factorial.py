# WAF to find the factorial of n. (n is the parameter)

def factorial (n):
    fact = 1
    for i in range (1,n+1,1):
        fact *= i
    return fact

n = int(input("n : "))
res = factorial(n)
print(res)