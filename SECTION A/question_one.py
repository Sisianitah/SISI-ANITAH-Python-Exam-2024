# (i)
#  Soln


import math


def circle_area(radius):

    pi = 3.14

    return math.pi * (radius ** 2)

radius = 4

area = circle_area(radius)

print(f"The area of a circle with radius {radius} is {area:.2f}")



# (ii)

# Soln

# the list

list = [4, 7, 2, 9, 12, 15]

numbers = [4, 7, 2, 9, 12, 15]

odd_sum = 0

for num in numbers:

    if num % 2 != 0:

        odd_sum += num

print("Sum of odd numbers:", odd_sum)



# (iii)   

# Soln 

def calculate(a, b):

    return a + b, a - b, a * b, a / b

sum_, diff, prod, quot = calculate(10, 2)

print(f"Sum: {sum_}, Difference: {diff}, Product: {prod}, Quotient: {quot}")



# (v)

#Soln

student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}

student_info['age'] = 26 

student_info['city'] = 'kampala'

print("The updated dictionary: ", student_info)




# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Sisianitah/SISI-ANITAH-Python-Exam-2024.git
# git push -u origin main
