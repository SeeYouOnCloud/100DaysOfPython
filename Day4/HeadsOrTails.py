#write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
import random

random_no = random.randint(0, 1)

if random_no == 1:
    print("Heads")
else:
    print("Tails")    