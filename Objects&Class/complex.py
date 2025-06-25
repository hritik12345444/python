# define a class for create a complex number than print sum of two complex number 
# dundar funtions hote hai printing ko normal print ki trah krane ke liye
class Complex:
    def __init__ (self,real,img):
        self.real= real
        self.img = img

    def showNumber(self):
        sign = "+" if self.img >= 0 else "-"
        print(f"{self.real}i {sign} {abs(self.img)}j")  # yeah pe self.img ka abs value print kraa rhe hai taki printing ke bich me do sign na aa jaye 
        # f ka use krte hai ki bich me koi value dal ske double quotes ke andar koi bhi value insert krr skte hai using curley braces{}
        # f ka matlba formated string hota hai



    # isme dundar function hai jiske wajah se normal printing hota hai 
    # def __add__(self,num2):  #sefl = num1 and num2 = num2
    #     newReal = self.real + num2.real
    #     newImg = self.img + num2.img
    #     return Complex(newReal,newImg)


    # yeah dundar function ka use nhi kiye hai isiliye add krane ke liye iss function me behjhna prega num1.add(num2)
    def add(self,num2): # yeah self me num1 aata hai 
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    

    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)

num1 = Complex(1,4)
num1.showNumber()

num2 = Complex(3,5)
num2.showNumber()

addition = num1.add(num2)  # funtion iska dundar function create nahi kiye hai 
addition.showNumber()

subtraction = num1 - num2  # this is subtraction of two numeber here funtion is a dunder function
subtraction.showNumber()


# this is use when we define a dunder function
# num3 = num1+num2
# num3.showNumber()