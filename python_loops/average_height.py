# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
num_of_students = 0
for i in student_heights:
  total_height += i
  num_of_students += 1
print(f"total height = {total_height}")
print(f"number of students = {num_of_students}")

# num_of_students = 0
# for j in student_heights:
#   num_of_students += 1
# print(f"number of students = {num_of_students}")

average_height = round(total_height / num_of_students)
print(f"average height = {average_height}")
