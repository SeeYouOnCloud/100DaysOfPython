#You are going to write a program that calculates the highest and lowest score from a List of scores.

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")      

lowest_score = student_scores[0]
for l_score in student_scores:
    if l_score < lowest_score:
        lowest_score = score
print(f"The highest score in the class is: {lowest_score}") 
'''
print(max(student_scores))
print(min(student_scores))
'''


#for loop with range() function
#for number in range(a, b)
for number in range(1, 10):
  print(number)

#for number in range(start, end, step by)
for number in range(1, 11, 3):
  print(number)

total = 0
for number in range(1, 101):
  total += number
print(total)    