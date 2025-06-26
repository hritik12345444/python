# Create a class called Order which stores item & its price.
# use Dunder function --gt--() to convey that:
# order1 > order2 if price of order1 > price of order2

# gt => greater than

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    # __gt__ ka matlab hota hai greater than ka method create krr rhe hai 
    def __gt__(self,ord2):    # __gt__ ka matlba hi hota hai ki > (iss function) ko call krr rhe hai
        ans = self.price > ord2.price
        return ans


ord1 = Order("tomato",250)
ord2 = Order("potato",130)
# ans = ord1.gt(ord2)   # this is for normal function not a dunder function
# print(ord1.gt(ord2))   #  this is for normal function not a dunder function
res = ord1 > ord2     # yeha function ka name nhi likhna hota hai kyuki isme hmm > find krr rhe hai aur uper ek funtion likhe hai __gt__ ka ye > (greter than ) ka hi logic ko define krrta hai
print(res)

# print(f"hello {res}")  print function ke andar f for formated string ke liye hota hai double quorts ke andar jo bhi likhye hai wo sbb ek string hota hai only jo curley brackets ke andar likhte hai ussse chod ke wo ek yessa cheez hota hai ki run time wha koi value dall skte hai