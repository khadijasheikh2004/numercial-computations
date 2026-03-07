# Bisection Method

import math

# take input function
f_str = input("Enter the function f(x) (e.g., x**3 + 4*x**2 - 10): ")

# convert string to function
def f(x):
    return eval(f_str)

# take inputs
a = float(input("Enter the first interval point a: "))
b = float(input("Enter the second interval point b: "))

tol = float(input("Enter tolerance (e.g., 1e-6): "))
max_iter = int(input("Enter maximum iterations: "))

# check interval validity
if f(a) * f(b) >= 0:
    print("\nInvalid interval: f(a) * f(b) >= 0")
    print("The function must have opposite signs at a and b.")
    exit()

# header 
print("\nIter\t a\t\t b\t\t m\t\t f(a)\t\t f(b)\t\t f(m)\t\t error(%)")

prev_m = a

# bisection method
for i in range(1, max_iter + 1):
    m = (a + b) / 2
    fa = f(a)
    fb = f(b)
    fm = f(m)

    # relative error
    error = abs((m - prev_m) / m) * 100

    # print
    print("%d\t %.6f\t %.6f\t %.6f\t %.6f\t %.6f\t %.6f\t %.6f" %
          (i, a, b, m, fa, fb, fm, error))

    # convergence check
    if abs(fm) < tol or abs(m - prev_m) < tol:
        print("\nConverged after", i, "iterations.")
        print("Approximate root:", "%.6f" % m)
        break

    # stop if repetition occurs
    if m == prev_m:
        print("\nRepetition detected. Stopping iterations.")
        print("Approximate root:", "%.6f" % m)
        break

    # update interval
    if fa * fm < 0:
        b = m
    else:
        a = m

    prev_m = m

else:
    print("\nMaximum iterations reached.")
    print("Approximate root:", "%.6f" % m)