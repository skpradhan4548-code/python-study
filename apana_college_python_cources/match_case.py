# This program just like in "C"language switch,case, difult !
day = int(input("enter the day number:"))

match day :
    case 1:
        print("sun_day")
    case 2:
        print("mon_day")
    case 3:
        print("Tuese_day")
    case 4:
        print("Wednes_day")
    case 5:
        print("Thus_day")
    case 6:
        print("Fri_day")
    case 7:
        print("Satur_day")
    case _:  # This is difult case like "C" program 
        print("Enterd wrong number")
