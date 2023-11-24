# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = input("Sample int: ")
a1 = int(n)
a2 = int(n + n)
a3 = int(n + n + n)
result = a1 + a2 + a3
print(f"Result of 'n+nn+nnn': {result}")
