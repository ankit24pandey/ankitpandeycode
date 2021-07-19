# TO PRINT RANDOM NUMBER-------------------------------------------------

import random
randomnumber=random.randint(1,11)
print(randomnumber)

# TO PRINT RANDOM THING FROM LIST--------------------------------------

l1=["star sports","republic bharat","sony","xyz","ten sports"]
choice=random.choice(l1)
print(choice)
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

