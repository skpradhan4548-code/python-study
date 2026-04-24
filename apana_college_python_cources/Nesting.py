username = input("enter the username:")
password = input("enter the password:")

if (username=="saroj" and password=="Saroj@2003"):
    print("Login succesfully")
else :
    if(username!="saroj"):
        print("enter wrong username")
    else:
        if(password!="Saroj@2003"):
            print("enterd wrong password")