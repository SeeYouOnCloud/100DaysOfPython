#Write a program that works out whether if a given number is an odd or even number
number = int(input("Which number do you want to check? "))

if(number % 2 == 0):
    print(f"{number} is a Even Number")
else:
    print(f"{number} is a Odd Number")    