import os

# specify the path of the directory you want to list
directory_path = "/"

try:
    # os.listdir() returns a list of filenames and folder names in the directory
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: The specified directory does not exist!")
except PermissionError:
    print("Error: Permission denied accessing the directory.")

