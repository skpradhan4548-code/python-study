class student:
    college_name = "COEB [College of Enginnering Bhubneswar]"   # This class
    college_Roll_no = "KGI202517559" # This is lower prierity 

    def __init__(self,Name,Roll_no,section):
        self.Name = Name   # This is instance 
        self.Roll_no = Roll_no
        self.section = section
        self.college_Roll_no = 2505219020 # This is higher prieriy 

stu1 = student("saroj",15,"B")
stu2 = student("Sandeep",12,"A")
stu3 = student("Shubham",10,"O")
stu4 = student("Saswat",8,"E")

print(student.college_name)
print(stu1.Name,stu2.Name,stu3.Name,stu4.Name)
print(stu1.college_Roll_no)