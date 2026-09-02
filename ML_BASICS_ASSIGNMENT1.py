
#1
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area =", area)

# 2
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)

# 3
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit =", fahrenheit)

# 4
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3

print("Average =", average)

# 5
n = float(input("Enter a number: "))

square = n * n
cube = n * n * n

print("Square =", square)
print("Cube =", cube)

# 6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("First number =", a)
print("Second number =", b)

# 7
# Student Report Program

name = input("Enter student name: ")
roll = input("Enter roll number: ")

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\nStudent Report")
print("Name:", name)
print("Roll Number:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)
