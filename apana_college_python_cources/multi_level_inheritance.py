class employee:
    stat_time = "10 AM"
    end_time = "6 PM"
    
class Adiministate(employee):
    def __init__(self,role):
        self.role = role

class Accountant(Adiministate): # That can be inherate all the parent class and child class
    def __init__(self,salary, role): 
        super().__init__(role)   # That supper() key word ae use for acces role properties of child class [Adiministate]
        self.salary = salary

acc1 = Accountant(70_000,"CA")

print(acc1.stat_time,acc1.end_time,acc1.salary,acc1.role)
