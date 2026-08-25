# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
# Your code here

a = 3.14,2.718,1.618,0.577
total = sum(a)
average = total/len(a)
print(average)

# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
# Your code here

f = 98.6
c = (f-32)*5/9
print(c)

# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
# Your code here

p = 1000
r = 5.5
t = 3
amount = p * (1+r/100)**t
compound_interest = amount-p
print(compound_interest)

# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
# Your code here

import math
a = 3.5
b = 4.2
c = math.sqrt(a**2 + b**2)
print(c)

# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
# Your code here

import math
r = 7.8
volume = (4/3) * math.pi * r**3
print(volume)

# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
# Your code here

number = 3.14159
result = round(number,3)
print(result)

# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
# Your code here

a = 45
b = 67
c = (a/b) * 100
print(c)

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
# Your code here

import math
a = 23.456
result = math.sqrt(a)
print(round(result,3))

# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
# Your code here

p = 2500
r = 6.5
t = 2.5
simple_interest = (p * t * r)/100
print(simple_interest)

# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
# Your code here 

import math
d = 45.7
radians = math.radians(d)
print(round(radians,3))
