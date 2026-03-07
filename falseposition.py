# False Position (Regula Falsi) Method

import math

# User Inputs
f_str = input("Enter the function f(x) (e.g., x**3 + 4*x**2 - 10): ")
a = float(input("Enter the first interval point a: "))
b = float(input("Enter the second interval point b: "))
tol = float(input("Enter tolerance (e.g., 1e-6): "))
max_iter = int(input("Enter maximum iterations: "))

# Function definition
def f(x):
    return eval(f_str)

# Check if root exists 
if f(a) * f(b) > 0:
    print("No root in the given interval!")
    exit()

print("\nIter\t a\t\t b\t\t c\t\t f(c)\t\t error(%)")

prev_c = a

for i in range(1, max_iter + 1):
    fa = f(a)
    fb = f(b)

    # Regula Falsi Formula
    c = b - fb * (a - b) / (fa - fb)

    # relative error
    error = abs((c - prev_c) / c) * 100

    print(f"{i}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}\t {error:.6f}")

    # Stopping condition
    if abs(f(c)) < tol:
        break

    # Update interval
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

    prev_c = c

print(f"\nApproximate root = {c:.6f}")
print(f"Number of iterations = {i}")