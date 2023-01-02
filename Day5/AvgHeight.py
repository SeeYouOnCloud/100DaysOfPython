#You are going to write a program that calculates the average student height from a List of heights.
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

#this is how sum() function works
total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height of students is {total_height}")   

#This is how len() function works
number_of_students = 0
for student in student_heights:
    number_of_students +=1
print(f"Number of students is {number_of_students}")  


'''
#if we use sum() len() function
total_height = sum(student_heights)
number_of_students = len(student_heights)
'''

average_height = round(total_height / number_of_students)
print(f"Average height of students is {average_height}")


