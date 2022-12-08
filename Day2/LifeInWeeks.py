#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
age = input("What is your current age? ")

years_remaining = 90 - int(age)
months = round(years_remaining * 12)
weeks = round(years_remaining * 52)
days = round(years_remaining * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")