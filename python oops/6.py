class Account:
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc

    def debit(self,amount):
        self.bal -= amount
        print(amount,"was debited")
        print("balance :",self.balance())
        print("\n \n")

        
    def credit(self,amount):
        self.bal += amount
        print(amount,"was crebited")
        print("balance :",self.balance(),"\n \n")

        
    def balance(self):
        return self.bal
        

obj = Account(10000,1234)
obj.debit(3000)
obj.credit(1500)
obj.credit(35000)
