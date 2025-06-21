
class Student:
    # name = "Hritik"   # for every student name is Hritik
    def __init__(self,fullname,marks):   # this is constructor
        self.name = fullname     # name and marks is attributes
        self.mark = marks
        print("adding new student ....")
    

s1 = Student("karan",333)
print(s1.name)
print(s1.mark)