import os

password = "admin123"

def run_command(cmd):
    os.system(cmd)

user_input = input("Enter command: ")
run_command(user_input)
