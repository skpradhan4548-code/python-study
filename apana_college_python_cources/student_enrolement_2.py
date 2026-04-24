# Create a dictionary from a list of tuples containing student names and subjects.
#  Store only unique subjects for each student using set. Print the final dictionary.
records = [
    ("Aman", "Math"),
    ("Riya", "Science"),
    ("Kabir", "English"),
    ("Aman", "English"),
    ("Riya", "Math"),
    ("Kabir", "Science"),
    ("Neha", "Hindi"),
    ("Aman", "Science"),
    ("Riya", "English"),
    ("Kabir", "Math"),
    ("Neha", "Math"),
    ("Aman", "Math"),
    ("Riya", "Science"),
    ("Kabir", "English"),
    ("Neha", "Science"),
    ("Arjun", "History"),
    ("Arjun", "Math"),
    ("Arjun", "Science"),
    ("Meera", "English"),
    ("Meera", "Hindi"),
    ("Meera", "English")
]

stu_dict = {}

for name,subject in records:
    if (stu_dict.get(name) == None):
        stu_dict.update({name:set()})
        stu_dict[name].add(subject)
    else:
        stu_dict[name].add(subject)

print(stu_dict)
