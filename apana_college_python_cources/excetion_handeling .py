try:
    x = int(input("enter the number of x: "))
    ans = 10/x
except ZeroDivisionError:
    print(f"Devide by zero is not allowed")
except ValueError:
    print(f"Invalid input")

else:
    print(f"ans = {ans}")

finally:
    print("The program are end ")