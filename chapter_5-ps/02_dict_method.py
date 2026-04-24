mark = {
    "saroj" : 200,
    "shubham" : 400,
    "sandeep" : 600,
    "saswet" : 800,
    1000 : "sana_mummy"
}

# print(mark,type(mark))
# print(mark["shubham"])
# print(mark.items())
# print(mark.keys())
# print(mark.update({"shubham":99}))
# print(mark)
# print(mark.update({"saswet":700,"sankar":100,"omm":50}))
# print(mark)

print(mark.get("kalia")) # prints None
# print(mark["kalia"]) # Returns error 
print(mark.pop("saroj"))
print(mark.popitem())