# Check you can vote or  not
# python is indentation based language (ye line ke phle space dena hai ya nhi ye sbb indentation hota hai )


age = int(input("age : "))
if(age >= 18):
    print("you can vote")
elif(age < 18 and age >= 17):
    print("you can you next year")
else:
    print("you can't vote")