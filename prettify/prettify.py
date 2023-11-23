import sys
from time import sleep


# TODO: Re-implement letter-by-letter some day in the future.
def ochprint(str, ms=0.02):
    for ch in str:
        sys.stdout.write(ch)
        sys.stdout.flush()
        sleep(ms)
