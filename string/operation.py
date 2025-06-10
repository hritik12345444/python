# Operation on string


str1 = "Hritik"
str2 = "singh"


#concateonation means add two string
str3 = str1+ " " + str2
print(str3)  # output is Hritik singh


# len(str3) gives us length of string
print(len(str3))


# \n is use for next line and \t is use for 4 space
sen = "Hello , My name is Hritik singh \nAnd i am a web developer student"
print(sen)


str = "apnaCollege"

#1. slicing
res = str[0:4] 
print(res)  # output is Apna


print(str[:4])  # output is Apna
print(str[4:12]) # output is College
print(str[4:]) # output is College
print(str[4: len(str)]) # output is College


# in python (-ve) indexing and (+ve) indexing both are allowed
print(str[-1]) #output is "e"
print(str[10])   #output is "e"


# sting function
print(str.endswith("ge")) # if str string is end with ge than it gives true else false
print(str.capitalize()) # first leter of str is capatilize
print(str.replace("ge","Hr")) # replace with old value to new value "ge" is old value and "hr" is new value
print(str.replace("a","H")) # replace with old value to new value "ge" is old value and "hr" is new value
print(str)
print(str.find("C")) # return 1st index of this char or word if it present in it else return -1
print(str.find("z")) # return 1st index of this char or word if it present in it else return -1
print(str.count("a"))  # reuturn count of this word or char, if that char is not present in it returns 0 