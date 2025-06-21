# Create Account class with 2 attributed - balance & account no.
# Create methods for debit,credit & printing the balance.


class Account:
    def __init__(self,acc_no, bal):
        self.Acc = acc_no
        self.balance = bal

    def debit(self,amount):
        return self.balance-amount
    
    def credit(self,amount):
        return self.balance+amount
    
    def balanceCheck(self):
        print("Your Acc:- ", self.balance)



acc = Account(12345,5555)
print(acc.balance)
print(acc.credit(1000))
print(acc.debit(3000))