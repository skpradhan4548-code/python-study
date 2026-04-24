class Bank_Account:
    def __init__(self,name,balance):
        self.name = name # This is public
      #  self._balance = balance # protect
        self.__balance = balance # This is private

    def get_balance(self): # getter
        return self.__balance
    
    def set_balance(self, new_balance): # setter
        self.__balance = new_balance

acc1 = Bank_Account("Saroj Pradhan",59_890)
acc1.set_balance(57_890)
print(acc1.name , acc1.get_balance())
print(acc1.name,acc1._Bank_Account__balance) # This is the second method that cna you see the balance with out any permision

    
