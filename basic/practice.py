#1. largest of three number

num1 = int(input("First no: "))
num2 = int(input("Second no: "))
num3 = int(input("Third no: "))

final_result = None
if(num1 > num2 and num1 > num3):
    final_result = num1
elif(num1 < num2 and num2 > num3):
    final_result = num2
else:
    final_result = num3

print(final_result)





#2. factorial of a number

num = int(input("Enter num: "))
fact = 1
while(num):  # while number is greater than 0
    print(num)
    fact *= num
    num-=1

print(fact)





#3. Check for prime number

num = int(input("Enter num: "))
i = 2
prime = "prime"
while(i <= num//2):
    if(num % i == 0):
        prime = "Not Prime"
        break
    else:
        i+=1

print(prime)





#4. fibonacci number

n = int(input("enter n: "))
i = 0
num1 = 0
num2 = 1
while(i < n):
    if(i == 0 or i == 1):
        print(i,end=" ") 
    else:
        next_num = num1 + num2
        print(next_num,end=" ")
        num1 = num2
        num2 = next_num
    i+=1





#5. Reverse a string

name = input("Enter name : ")
rev_name =""
i = len(name) - 1
while(i >= 0):
    rev_name += name[i]
    i-=1

print(rev_name)

name2 = name[::-1]  # this is a slicing method of string. Basically name string ko uthao aur reverse krr do yehi hai iska matlab

print(name2)





#6. Count vowel in a string
sentence = input("sentenct : ")
i = 0
count = 0
while(i < len(sentence)): 
    if(sentence[i] == 'a' or sentence[i] == 'e' or sentence[i]== 'i' or sentence[i]== 'o' or sentence[i] =='u'):
        count += 1
    i += 1

print(count)





#7. find maximum element in a list

my_list =[33,4,5,6,14,3,5,4,6,4,38]
max_ele = my_list[0]
i = 1
while(i < len(my_list)):
    if(my_list[i] > max_ele):
        max_ele = my_list[i] 
    i+=1

print(max_ele)





# 8 Remove duplicates from a list. We have three method for doing this
# method 1   normal iterative way
my_list = [1,1,2,4,6,5,4,6,73,6,9,7,4,2,6]
unique_list = []
for ele in my_list:
    if ele not in unique_list: # means agar ele nahi hai unique_list me to ye condition true hoga
        unique_list.append(ele)
print(unique_list)

# Method 2  using dictionary because dictionary store a unique key not unique value. Hmm yaha pe key me store kiye hai vaue ko
my_list2 = [1,1,2,4,6,5,4,6,3,6,9,7,4,2,6]
unique_list2 = list(dict.fromkeys(my_list2))  # my_list2 ko ek dictionary ke key me store kiye iske wajah se unique element key me store hoga uske badh list me typeCast krr diye to unique element store hogya hai
print(unique_list2)

# Method 3  using set because set store unique value
my_list3 = [1,1,2,4,6,5,4,6,3,6,9,7,4,2,6]
unique_list3 = list(set(my_list3))  # list ko set me daal diye fir list me typecast krr diye . Set me unique value store hota hai
print(unique_list3)



# 10. Print a triangle pattern
n = int(input("enter no of lines : "))
i = 1
while(i < n):
    j = 1   
    while(j <= i):
        print('💛💛💛',end="  ")
        j+=1
    i+=1
    print("\n")