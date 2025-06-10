# semicolon is not compulsory in python 
# if we write multiple statement in one line than we use semicolon for seperate that statement


print("Hritik is my name.", "I am 20 years old ")
print("I am a bca student of last year")

a= 3; b="&"; c= 2
print(a*b*c)  # expected output is a*c=  6 * b = dddddd

d="Hritik"; e=" singh"
print(d+e)  # expected output is Hritik singh

# int + float = floar
f=3; g=2.0
print(f+g)   # expected output is 5.0 
print(f-g)   # expected output is 1.0
print(f*g)   # expected output is 6.0
print(f/g)   # expected output is 1.5
print(f%g)   # expected output is 1.0   search on chatGpt
print(f//g)  # expected output is 1.0    this is integer division, integer division answer ko float se int me change krr dega lekin output me answer float me dikhega like 4.6=> 4.0, 0.5=>0.0, so on.....
print(1.5 // 3)  # expected output is 0.0  this is integer division, integer division answer ko float se int me change krr dega lekin output me answer float me dikhega like 4.6=> 4.0, 0.5=>0.0, so on.....

# floor value jo answer dega whi integer division bhi answer dega ex => (1.5 // 3) => 0.0 , and floor (1.5/3) => 0.5 => floor of 0.5 is 0.0

# V.V.I  if denominator is negative than modulo operator give me in negative value
print(5 % 2)  # expected output is (num(+)  and den(+)) so output is (+ve)
print(-5 % 2) # expected output is (num(-)  and den(+)) so output is (+ve) 
print(5 % -2) # expected output is (num(+)  and den(-)) so output is (-ve)
print(-5 % -2) # expected output is (num(-)  and den(-)) so output is (-ve)