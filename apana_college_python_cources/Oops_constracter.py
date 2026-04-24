class student:
    def __init__(self,name,subject,cgpa):  # This aa constrctor
        self.name = name          #|| The assign the name in the memory location      ||-------------------------------
        self.subject = subject    #|| Tha assign the subject in the memory location   ||  This are instance attributes
        self.cgpa = cgpa          #|| The assign the cgpa in the memory location      ||-------------------------------
            
    def get_cgpa(self):        # This is instance method 
        return self.cgpa

stu1 = student("Saroj","chemistry",7.99)
stu2 = student("Sandeep","Physics",9.54)
stu3 = student("Shubham","English",8.32)
stu4 = student("Saswet","Odia",8.22)

# class student:
#     def __init__(self):     [This is a defult constructer]
#         print("This constracter let's use it")

# stu1 = student()

print(stu1.name,stu1.subject)
print(stu2.name,stu2.subject)
print(stu3.name,stu3.subject)
print(stu4.name,stu4.subject)

print(stu3.cgpa)
print(f"{stu3.name} has cgpa = {stu3.get_cgpa()}")