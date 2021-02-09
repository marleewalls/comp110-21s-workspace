"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730225231"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
num: int = randint(1, 10)
print("Your fortune cookie says...")
if num < 3:
    print("you will have a good day")
elif num < 6:
    print("you will have a good year")
elif num < 8:
    print("you will have a good decade")
else:
    print("you will have a good life")
print("Now, go spread some positive vibes!")
