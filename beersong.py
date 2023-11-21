"""
Fist "Program" to remember HOW TO CODE.
Generate song about beer with right bottle count and word forms.
 From "Head First Python 2 edition" by Paul Berry
"""
from prettify import ochprint

word = "bottles"
for bottles_num in range(99, 0, -1):
    ochprint(f"{bottles_num} {word} of beer left on the wall!\n", 0.02)
    ochprint(f"{bottles_num} {word} of beer.\n")
    ochprint("Take one down.\n")
    ochprint("Pass it around.\n")
    print("---------------")
    if bottles_num == 1:
        ochprint("No more bottles left on the wall...\n")
    elif bottles_num == 2:
        ochprint(f"{bottles_num} bottle of beer on the wall!\n")
