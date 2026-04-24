import os

# Specify the directory path
path = "/"

# List and print contents of the directory
print("Contents of the directory are:")
for item in os.listdir(path):
    print(item)
