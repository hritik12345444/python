# Create student class that takes name & marks of 3 subjects as arguments in construcotr
# Then creat a mehod to print the average

class student:   # this is class
    def __init__(self,name,phy,che,math):   # this is constructor
        self.name = name
        self.phy = phy
        self.che = che
        self.math = math
        print("object is created ...")
        
    def average(self):   # this is method for calculate some operations
        avg = (self.phy + self.che + self.math)/3
        return avg
    

s1 = student("Hritik",88,57,85)
avg = s1.average()
print(int(avg))   # print average in integer value
