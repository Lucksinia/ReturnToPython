"""
Fist "Program" to remember HOW TO CODE.
Generate song about beer with right bottle count and word forms.
 From "Head First Python 2 edition" by Paul Berry
"""

import sys
from time import sleep

# TODO: Re-implement letter-by-letter some day in the future.
def ochprint(str, ms=0.02):
    for ch in str:
        sys.stdout.write(ch)
        sys.stdout.flush()
        sleep(ms)


word = "bottles"
for bottles_num in range(99, 0, -1):
    ochprint(f"{bottles_num} {word} of beer left on the wall!\n")
    ochprint(f"{bottles_num} {word} of beer.\n")
    ochprint("Take one down.\n")
    ochprint("Pass it around.\n")
    print("---------------")
    if bottles_num == 1:
        ochprint("No more bottles left on the wall...\n")
    elif bottles_num == 2:
        ochprint(f"{bottles_num} bottle of beer on the wall!\n")
