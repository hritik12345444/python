# Write a recursive function to calculate the sum of first n natural numbers.


def calSumNatural(n):
    if(n == 0):
        return 0
    sum = calSumNatural(n-1) + n
    return sum

n = int(input("n : "))
res = calSumNatural(n)
print(res)