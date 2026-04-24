# square = [i*i for i in range(6)] # That print the square root of 0-5 number 
# print(square)

#===================================================================================================================== 
# square = [i*i for i in range (6) if i%2 != 0] # That logic is show that the only odd number can show the square root

# print(square)
#=======================================================================================================================
# num = [-5,7,9,-6,2,-1,-4,4]
# num = [0 if value<0 else value for value in num ]  # it menas that the value shoud be zero then it can ok but if less than then remove that element 
#                                                   # it can be add the zero on the perticular spcae 


# print(num)
#==============================================================================================================================
words = ["hello","saroj","kalia"]

# print(words[1].upper())  # This is one by one can change the word lower to upper 

words = [val.upper() for val in words]
print(words)