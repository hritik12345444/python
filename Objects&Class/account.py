# Create Account class with 2 attributed - balance & account no.
# Create methods for debit,credit & printing the balance.


class Account:
    def __init__(self,acc_no, balance):
        self.Acc = acc_no
        self.balance = balance

    def debit(self,amount):
        print("your acc is debited by Rs :-",amount)
        self.balance = self.balance - amount
        print("your current balence is Rs :-",self.balance)
    
    def credit(self,amount):
        print("Your acc is credited by Rs :-",amount)
        self.balance = self.balance + amount
        print("your current balence is Rs :-",self.balance)
    
    def balanceCheck(self):
        print("Your total-balence is Rs :- ", self.balance)



a = Account("12345",4000)
a.credit(1000)
# a.debit(2000)
# a.balanceCheck()