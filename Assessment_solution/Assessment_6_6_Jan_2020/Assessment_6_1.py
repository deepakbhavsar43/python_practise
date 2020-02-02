"""
Write a program which accepts file name from user and check whether that file exists in current directory or not.
Input: Demo.txt
Check whether Demo.txt exists or not.
"""

import os.path

# f_name = 'Demo.txt'
f_name = input("Enter the name of file you are looking for : ")
result = os.path.exists(f_name)
if result == True:
    print(f"\nFile exists in current directory\n{os.path}")
else:
    print("File not found.")