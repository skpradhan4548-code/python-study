class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):               #================
    def get_designation(self):         #  Over riding  =
        print("designation = Teacher") #================
