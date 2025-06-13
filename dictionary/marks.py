# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.


my_dict = {} # intialize a empty dictionary

phy = input("phy : ")
my_dict.update({"phy" : phy})

chem = input("chem : ")
my_dict.update({"chem": chem})

math = input("math : ")
my_dict.update({"math" : math})

print(my_dict)