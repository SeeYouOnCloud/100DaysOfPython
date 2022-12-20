#https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
#https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators

import random

#randint returns a random integer between a and b (both inclusive). This also raises a ValueError if a > b.
random_integer = random.randint(1, 10)
print(random_integer)

#random.random() -> Returns the next random floating point number between [0.0 to 1.0)
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}%")