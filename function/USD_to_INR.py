# WAF to convert USD to INR


def convertUSD(usd):
    return usd*86.11


USD = int(input("USD : "))
INR = convertUSD(USD)
print(INR)