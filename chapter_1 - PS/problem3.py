import os

# specify the directory path you want to list
directory_path = "/"

try:
    # listdir() returns a list of entries in the directory
    contents = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist!")
except PermissionError:
    print("Permission denied – cannot access this directory.")
