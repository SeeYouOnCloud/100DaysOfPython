import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(names)
num_items = len(names)

#last item -> (num_items -1)
random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")