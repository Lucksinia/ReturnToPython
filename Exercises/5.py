# 5. Write a Python program that accepts the user's first and last name and prints them
# in reverse order with a space between them.
name = input("Please, input your name and shurname: ").split(" ")
print(f"{name[1]} {name[0]}")
