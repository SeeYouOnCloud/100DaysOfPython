#https://docs.python.org/3/tutorial/datastructures.html

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina"]

#fetch the items using index number(programmers start counting from 0)
print(states_of_america[0])

#find out length of list
print(len(states_of_america))

#-1 will start counting from end
print(states_of_america[-1])

#replace the items
states_of_america[2] = "Missouri"
print(states_of_america)

#add item in existing list ..it will be added at the end
states_of_america.append("California")
print(states_of_america)

#add whole bunch of data in an existing list
states_of_america.extend(["Montana", "Washington", "Idaho", "Wyoming", "Utah"])
print(states_of_america)

