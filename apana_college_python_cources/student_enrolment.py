info =[
    ("Alice","math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charli","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("charli","English")
]
# course_set= set()

# for name,course in info:
#     print(name,course)
#==================================================================
# List all unique course (Problem-1)
# unique_courese = set()
# for tuple in info:
#     # print(tuple[0])  # Name 
#     # print(tuple[1])  # Course
#       unique_courese.add(tuple[1])
# print(unique_courese)
#==============================================================
# List student enrolled in physics (Problem-2)
# for name,course in info:
#     if (course=="physics"):
#         print(name)
#==============================================================

dict = {}

for name ,course in info :
    if( dict.get(name)== None):
        dict.update({name :set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)


    
