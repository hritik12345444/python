# dictionary in Python
# for initialization of dictionary


# dictionary store key value pair
# Each key unique in dictionary
# Each key is associated with a value
# Dictionary are unordered
# They are mutable, meanign you can chage them after creation

my_dict= {
    "Name" : "Hritik",
    "Course" : "BCA",
    "Roll no" : 37
}

# print(list(my_dict)) # Typecaste the my_dict into list
# print(my_dict)
# print(type(my_dict))
# print(my_dict["Name"])
# print(my_dict["Course"])
# print(my_dict["Roll no"])

my_dict2 = {
    "name" : "Shatrudhan",
    "Class" : 12,
    "subject" : {
        "phy" : 88.4,
        "chem" : 94,
        "math" : 100
    },
    "about" : "Student"
}

print(my_dict2["subject"]["chem"])  # accessing the marks of chem this is for nested dictionary
print(my_dict2.keys())
print(my_dict2.values())

print(my_dict2["about"])   # if about key is not found in my_dict2 than gives me a error , to isiliye 2nd option best hota hai jada files honge dict me to search krne ke liye
print(my_dict2.get("about"))  # output is student
print(my_dict2.get("loved"))  # output is None because loved is not present in my_dict2 # agar 


my_dict2["level"] = "super"  # if level key is not present in dict than it will add in that dict , if level is present in dict than it will update this 
print(my_dict2)
del my_dict2["about"]  # delet the key from dictionary
print(my_dict2)

my_dict2.update({"syco" : "Shubham"}) # agar ye value dictionary me nhi rha to add krr dega agar rha to overwrite krr dega
print(my_dict2["syco"])






print("The End")