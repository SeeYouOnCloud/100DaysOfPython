'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#weight divided by the height to the power of 2
#round function is gonna round the value to the nearest whole number
bmi = round(weight / height ** 2)
#first if statement is checked if that fails only then it will go to elif statement. The statement will be checked one by one in order 
if bmi  < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.") 
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")