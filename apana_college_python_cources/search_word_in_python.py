data = True
line = 1
word = "kalia"

with open("apana_college_python_cources/sample.txt","r") as f:
    while data:
        data = f.readline()

        if(word in data):
            print(f"{word} found in line no :{line}")
            break
        line+=1