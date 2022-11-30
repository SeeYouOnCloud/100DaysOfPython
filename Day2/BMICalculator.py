#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight = int(weight)
height = float(height)

bmi = weight / height ** 2

bmi = weight / (height * height)

bmi_as_int = int(bmi)

print(bmi_as_int)