student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height= 0

for heights in student_heights:
  total_height += heights

number = 0
for student in student_heights:
  number += 1

avg = round(total_height / number )
print(avg)