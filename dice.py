#!/usr/bin/env python3

import random


exit = "q"
n = random.randint(1,6)
value = input("please type anything except q to roll a dice\n")
print(n)
while value != exit:
    value = input("please type anything except q to roll a dice\n")
    print(n)
print("you have sucessfully exited the game")

