# Write a Python program that accepts a sequence of comma-separated numbers from the
# user and generates a list and a tuple of those numbers.

inpt = input("Input numbers throug commas: ")
lst = list(inpt.split(","))
tpl = tuple(lst)
print(lst)
print(tpl)
