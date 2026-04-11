# Linear Interpolation 
import math

# input 
f_str = input("Enter function f(x): ")

def f(x):
    return eval(f_str)

# point to interpolate
xp = float(input("Enter point to interpolate (x): "))

# initial conditions
x0 = float(input("Enter x0: "))
x1 = float(input("Enter x1: "))

# compute f values
f0 = f(x0)
f1 = f(x1)

# linear interpolation formula 
# f(x) ≈ f(x0) + [(f(x1) - f(x0)) / (x1 - x0)] * (x - x0)

interp = f0 + ((f1 - f0) / (x1 - x0)) * (xp - x0)

# true value 
true_val = f(xp)

# error analysis 
abs_error = abs(true_val - interp)

if true_val != 0:
    rel_error = abs_error / abs(true_val) * 100
else:
    rel_error = 0

# output 
print(f"\nInterpolated value = {interp:.6f}")
print(f"True value         = {true_val:.6f}")
print(f"Absolute Error     = {abs_error:.6f}")
print(f"Relative Error (%) = {rel_error:.6f}")