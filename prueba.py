import os

def unsafe_function():
    password = input("Enter password: ")
    os.system(f"echo {password}")

unsafe_function()
