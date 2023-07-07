"""
TODO: It
This is snake game implimentation with the help of 
blessed module https://pypi.org/project/blessed/
"""

from blessed import Terminal

term = Terminal()
with term.location(0, term.height - 1):
    print("This is " + term.underline("underlined") + "!", end="")
