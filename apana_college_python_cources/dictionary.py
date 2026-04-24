# crate a dictionary on student table 

info = {
    "Student 1": " Saroj Pradhan",
    "Branch1":  "MCA",
    "Roll number" : "KGI@25506",
    "CGPA 1" : "8.04",
  "Student 2": " Sandeep Pradhan",
    "Branch2":  "MBA",
    "Roll number" : "KGI@2789",
    "CGPA 2" : "9.04",
  "Student 3": " Shubham Pradhan",
    "Branch3":  "M-Tech",
    "Roll number" : "KGI@2356",
    "CGPA 3" : "7.98"  
}

# info["CGPA 1"] = "10.00" # The dictionary are imutable 
print(type(info))

# print(info["Student 1"]) # I maupulate the data on my self 
# print(info["CGPA 1"])

#==========================================================================
# THE OPERATION ARE PERFERMED ON DICTIONARY #
#==========================================================================

# print(info.keys())
# dict_keys = list(info.keys()) # convert in to list 

# print(dict_keys)

# print(type(dict_keys)) # Print types

# dict_values = list (info.values()) # print all the value in dictionary 
# print(dict_values) # print all the values 

# dict_items = info.items() # display all the intem are exixst in the dictionary

# print(list(info.items()))

# dict_get = info.get("Branch3")
# print(dict_get)
# info.update({   
#    "Student 4": " Saswat Pradhan",
#     "Branch4":  "B-Tech",
#     "Roll number" : "KGI@4657",
#     "CGPA 4" : "8.43"     
# })

# info.update({
#     "Student 5": " Ritu_rani Pradhan",
#     "Branch5":  "CT",
#     "Roll number" : "KGI@654",
#     "CGPA 3" : "9.7"  
# })

# print(info)