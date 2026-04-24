a = 10
b = 20

sum = a+b

# # normal formaing
# print("sum of {} & {} is {}".format(a,b,sum))
# print("The language i use is{}".format("python"))

# index based formating
# print("sum of {1} and {0} is {2}".format(a,b,sum))

# Value based formating 

# print("value of a is {} and b{} is ".format(a=50,b=30)) // error is formed 
print("value of a is {} and b {} is {}".format(50, 30, 50 + 30))
print("value of a is {a} and b {b} is {sum} ".format(a=50, b=30, sum=50 + 30))
print("value of {a} and {b} is {sum}".format(a= 30,b= 40,sum= 30+40))
print("value of {} and {} is {}".format(30,60,60-30))
