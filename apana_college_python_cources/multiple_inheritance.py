class Teacher:
    def __init__(self,salary):
        self.salary = salary

class student:
    def __init__(self,gpa):
        self.gpa = gpa

class TA(Teacher,student):
    def __init__(self, salary,gpa,name): # This is the sub-class of child
        super().__init__(salary) # That inherate child class
        student.__init__(self,gpa)
        self.name = name

ta1 = TA(12_000,9.7,"Saroj_Pradhan")

print(ta1.salary,ta1.name,ta1.gpa)