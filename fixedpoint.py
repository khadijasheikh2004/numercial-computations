# Fixed Point Method

import math

# take input function g(x)
f_str = input("Enter the iteration function g(x) (e.g., (10/(x+4))**0.5): ")

# convert string to function
def g(x):
    return eval(f_str)

# take inputs
x0 = float(input("Enter initial guess x0: "))
tol = float(input("Enter tolerance (e.g., 1e-6): "))
max_iter = int(input("Enter maximum iterations: "))

# header
print("\nIter\t x\t\t error(%)")

# fixed point iteration
for i in range(1, max_iter + 1):
    x1 = g(x0)

    # relative error
    error = abs((x1 - x0) / x1) * 100

    print("%d\t %.6f\t %.6f" % (i, x1, error))

    # stopping condition
    if abs(x1 - x0) < tol:
        print("\nConverged.")
        print("Approximate root = %.6f" % x1)
        print("Number of iterations =", i)
        break

    x0 = x1

else:
    print("\nMaximum iterations reached.")
    print("Approximate root = %.6f" % x1)