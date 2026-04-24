class Employee:
    start_time = "10 AM"
    end_time = "6 PM"

    def change_time(self,new_end_time):
        self.end_time = new_end_time

class Teacher(Employee): # child class inherte Employe class  
    def __init__(self,Subject):
        self.Subject = Subject

class Adminstaff(Employee):  # child class inherte Employe class   
    def __init__(self,role):
        self.role = role
    

t1 = Teacher("Mathmatics")
t1.change_time("5 PM")
print(t1.Subject,t1.start_time,t1.end_time)
staff1 = Adminstaff("manager")

print(staff1.role,staff1.start_time,staff1.end_time)