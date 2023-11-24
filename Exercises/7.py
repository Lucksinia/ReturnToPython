# 6. Write a Python program that accepts a filename from the user and prints the
# extension of the file.

file = input("Please input full filename: ")
suff = file.split(".")
print(suff[1])
