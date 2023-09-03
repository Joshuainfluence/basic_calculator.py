# basic calculator
from math import *
print("Let's perform some basic arithmetics") 

x = input("Enter number: ")
y = input("Enter another number: ")

# we use float function so as to be able to solve both integers and decimal numbers
z = float(x) + float(y)
a = float(x) * float(y)

# the string function is called because we are concatenating 
# the ceil function is to remove the number after the decimal
print("The sum of " + str(x) + " and " + str(y) + " is " + str(ceil(z)))
print("The Product of " + str(x) + " and " + str(y) + " is " + str(ceil(a)))

