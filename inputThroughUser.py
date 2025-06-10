# Taking input form user

# in this code input function is use to take input from user and store tham into name variable 
name = input("Enter name : ") # in input, name is displayed on output terminal 

# by default input krte hai kisi bhi cheeze ko to wo ek string ke rup me input hota hai. Hmme usee int ya float ya etc me change krne ke liye typecaste krna hota hai 


age = int(input("Enter age : "))  # strirng ko int me typecaste krr diye hai 
price = float (input ("Enter prince of bruse : "))


# print output
print("My name is -> " , name) 
print("My age is -> ",age , "years old")
print("price of my bruse -> ",price)


# print the type of input  
print(type(name))
print(type(age))
print(type(price))