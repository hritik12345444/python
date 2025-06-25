# Define a Employee class with attributed role, department & salary. This class also have a method showdDetails() method.
# Create an engineer class that inherits properties from Employee & has additional attributes : name & age 


class Employee:
    def __init__(self,role,dpart,slry):
        self.role = role
        self.dpart = dpart
        self.slry = slry


    def showDetails(self):
        print("Role:-",self.role)
        print("Department:-",self.dpart)
        print("Salary:-",self.slry)



class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","60,000")


    

emp = Employee("Sister","ICU","25,000")
# emp.showDetails()


eng = Engineer("Hritik",20)
# eng.showDetails()