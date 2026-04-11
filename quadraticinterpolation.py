# Quadratic Interpolation 

import math

# input 
f_str = input("Enter function f(x): ")

def f(x):
    return eval(f_str)

# point to interpolate
xp = float(input("Enter point to interpolate (x): "))

# input points
x0 = float(input("Enter x0: "))
x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))

# function values 
f0 = f(x0)
f1 = f(x1)
f2 = f(x2)

# newton's divided difference formula
b0 = f0
b1 = (f1 - f0) / (x1 - x0)
b2 = ((f2 - f1) / (x2 - x1) - b1) / (x2 - x0)

interp = b0 + b1*(xp - x0) + b2*(xp - x0)*(xp - x1)

# true value 
true_val = f(xp)

# error analysis 
abs_error = abs(true_val - interp)

if true_val != 0:
    rel_error = (abs_error / abs(true_val)) * 100
else:
    rel_error = 0

# output 
print(f"\nInterpolated value = {interp:.6f}")
print(f"True value         = {true_val:.6f}")
print(f"Absolute Error     = {abs_error:.6f}")
print(f"Relative Error (%) = {rel_error:.6f}")