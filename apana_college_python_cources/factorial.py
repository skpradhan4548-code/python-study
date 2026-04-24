

def caluclate_fact(n):
    fact = 1
    for i in range(1,n+1):
      fact*=i
    return fact

n = int(input("enter the number(n):"))
print(caluclate_fact(n))