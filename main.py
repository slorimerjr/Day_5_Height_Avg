# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights (in cm) ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
height_total = 0
for x in range(0, n + 1):
  height_total += student_heights[x]

print(f"The height average of the class is {int(height_total / (n + 1))}.")


