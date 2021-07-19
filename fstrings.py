"""import math     # MODULE MATH #
me="ankit"
a=24
x=f"this is {me} {a} {math.cos(0)}"
print(x)"""
# FUN GAME--- GIVE INPUT ANYTHING FROM(WATER/GUN/SNAKE) AND COMPUTER ALSO PRINT SOMETHING RANDOM FROM(WATER/GUN/SNAKE)-----------------------
import random
l=("snake","water","gun")
choice=random.choice(l)
# print(choice)
print("enter user choice")
n=input()
if n==choice:
    print("draw")
elif n=="water" and choice=="snake":
    print("computer win")
elif n=="snake" and choice=="water":
    print("you win")
elif n=="gun" and choice=="snake":
    print("you win")
elif n=="snake" and choice=="gun":
    print("computer win")
elif n=="water" and choice=="gun":
    print("computer win")
elif n=="gun" and choice=="water":
    print("you win")
else:
    print("error")
print("computer choice is",choice)
