"""
Fist "Program" to remember HOW TO CODE.
Generate song about beer with right bottle count and word forms.
 "Head First Python"
"""
import threading

# implement letter-by-letter some day in the future.
def ochprint(str, ms=1):
    pass


word = "bottles"
for bottles_num in range(99, 0, -1):
    print(f"{bottles_num} {word} of beer left on the wall!")
    print(f"{bottles_num} {word} of beer.")
    print("Take one down.")
    print("Pass it around.")
    print("---------------")
    if bottles_num == 1:
        print("No more bottles left on the wall...")
    elif bottles_num == 2:
        print(f"{bottles_num} bottle of beer on the wall!")
