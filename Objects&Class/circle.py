# Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of teh circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.


import math # for using math function
class Circle:
    def __init__ (self,rad):
        self.rad = rad

    def Area(self):
        ara=  math.pi * self.rad ** 2 # (22/7 * r * r ) we can able to do this because we import math
        print(f"Area = {ara} cm^2")
    
    def Perimeter(self):
        pere = 2 * 22/7 * self.rad
        
        print(f"Perimeter = {pere} cm")
    

c1 = Circle(5)
c1.Area()
c1.Perimeter()

c2 = Circle(10)
c2.Area()
c2.Perimeter()

pi = math.pi # this is exact value of pi 
print(pi)