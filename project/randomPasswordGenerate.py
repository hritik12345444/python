# Random password generate of n digit (password should be the combination of character , digit, punctuations)

import random   # this is for select random character form pswd
import string   # this is for make a string with letter digit punctuation

n = int(input("size of password : "))
pswd = string.ascii_letters + string.digits + string.punctuation  # pswd me total alphabet small and capital , total number 0 to 0 and all special charecter (punctuation)

i = 1
password =""
while(i <= n):
    password += random.choice(pswd)
    i += 1


print(f"Your password :-  {password}")