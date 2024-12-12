# (i)

# Soln

name = input("Enter student name: ")
student_number = input("Enter student number: ")
programming = int(input("Enter Programming marks: "))
data_science = int(input("Enter Data Science marks: "))
computer_applications = int(input("Enter Computer Applications marks: "))
average_mark = (programming + data_science + computer_applications) / 3

print(f"Student Name: {name}")
print(f"Student Number: {student_number}")
print(f"Programming: {programming}")
print(f"Data Science: {data_science}")
print(f"Computer Applications: {computer_applications}")
print(f"Average Mark: {average_mark:.3f}")





#(iii)

# Soln


miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallons used: "))

mpg = miles_driven / gallons_used
print(f"The car's MPG (miles per gallon) is: {mpg:.2f}")








# (iii)

#Soln

for num in range(1, 102):
    if num % 2 != 0:
        print(num, end=" ")