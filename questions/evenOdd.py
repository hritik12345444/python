# Check if a number is even or odd
num = int(input("num : "))
print("even") if(num%2==0) else print("odd")




# find the sum of numbers from 1 to 100
sum = 0
for i in range(1,101,1):
    sum+= i
print(sum)




# reverse a string
name = input("name : ")
reversed_text = "" # initialize a inpty text area
for char in name:  # char in 1st character aayega name ka 
    reversed_text = char + reversed_text # 1st char aayega reversed text me ussse add krr denge
    # name = hello
    # ""
    # h + "" = h
    # e + h = eh
    # l + eh = leh
    # l + leh = lleh
    # o + lleh = olleh
print(reversed_text)





# Find the largest number among three
num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
num3 = int(input("num3 : "))

largest = num1
if(num1 > num2 and num1 > num3):
    largest = num1
elif(num2 > num1 and num2 > num3):
    largest = num2
else:
    largest = num3

print(largest)





# check if a number is positive,negative, or zero
num = int(input("num : "))
if(num > 0):
    print("Positive")
elif(num < 0):
    print("Negative")
else:
    print("Zero")





# Count the number of vowels in a string
word = input("word : ")
count = 0
for char in word :
    if(char == 'a' or char =='e' or char == 'i' or char == 'o' or char =='u'):
        count+=1

print(count)






# Check if a string is a palindrome
word = input("word : ")
word2 = ""
for char in word:
    word2 = char + word2
if(word == word2):
    print("yes , it is palindrome")
else:
    print("Not , palindrome")





# swap two numbers
num1 = int(input("num1 : ")) 
num2 = int(input("num2 : "))

# method 1
# temp = num1
# num1 = num2
# num2 = temp

# method 2
num1 = num1+num2
num2 = num1 - num2 
num1 = num1 - num2

print("num1 is " ,num1)
print("num2 is ",num2)