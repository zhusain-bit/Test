#This program is intended to solve for the roots of a quadratic formula
# after it is given the coefficients in the quadratic equation.
#This program will include info regarding the number of real and imaginary solution
import math
#input a, b, and c values of quadratic
x = int(input("How many quadratics will you solve?"))

#for loop will run for the amount of times that the user inputs
for i in range(0, x):
    a = float(input("Enter your a value: "))
    b = float(input("Enter your b value: "))
    c = float(input("Enter your c value: "))
#determine number of real/imaginary roots based on value of discriminant
    value = b**2 - 4*a*c
    #checking if the discriminant is negative
    if value < 0:
        imaginary = 2
        real = 0
    #solve for roots
        x1 = (-b+math.sqrt(-1*value))/2*a
        x2 = (-b-math.sqrt(-1*value))/2*a
        print ("x = ", x1, "i, ", x2, "i")
        print ("number of real solutions:", real, "\n", "number of imaginary solutions:", imaginary)
        #checking if discriminant is positive
    elif value > 0:
        imaginary = 0
        real = 2
        x1 = (-b+math.sqrt(value))/2*a
        x2 = (-b-math.sqrt(value))/2*a
        print ("x = ", x1,",",x2,)
        print ("number of real solutions:", real, "\n", "number of imaginary solutions:", imaginary)
        #if neither positive nor negative, the discriminant must be zero, and there must be one real solution
    elif value == 0:
        imaginary = 0
        real = 1
        x1 = (-b+math.sqrt(value))/2*a
        print ("x = ", x1)
        print ("number of real solutions:", real)