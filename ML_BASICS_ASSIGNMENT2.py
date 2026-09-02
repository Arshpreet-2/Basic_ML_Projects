# 1
total = 0

for i in range(1, 11):
    total = total + i

print(total)

# 2
n = int(input("Enter number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)

# 3
n = int(input("Enter number of terms: "))

first = 0
second = 1

for i in range(n):
    print(first, end=" ")
    
    next = first + second
    first = second
    second = next

# 4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

# 5
name = input("Enter name: ")
roll = input("Enter roll number: ")

total = 0
subjects = 5

for i in range(subjects):
    marks = float(input(f"Enter marks of subject {i+1}: "))
    total += marks

percentage = total / subjects

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\nStudent Result")
print("Name:", name)
print("Roll No:", roll)
print("Percentage:", percentage)
print("Grade:", grade)


