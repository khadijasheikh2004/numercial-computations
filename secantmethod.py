# Secant Method

import math

# input function
f_str = input("enter function f(x): ")

# convert string to function
def f(x):
    return eval(f_str)

# take inputs
x0 = float(input("enter first guess x0: "))
x1 = float(input("enter second guess x1: "))
tol = float(input("enter tolerance: "))
max_iter = int(input("enter maximum iterations: "))

# header
print("\niter\t x\t\t f(x)\t\t error(%)")

for i in range(1, max_iter + 1):

    fx0 = f(x0)
    fx1 = f(x1)

    # secant formula
    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

    # relative error
    error = abs((x2 - x1) / x2) * 100

    print("%d\t %.6f\t %.6f\t %.6f" % (i, x2, f(x2), error))

    # stopping condition
    if abs(x2 - x1) < tol:
        print("\nconverged.")
        print("approximate root = %.6f" % x2)
        print("number of iterations =", i)
        break

    # update values
    x0 = x1
    x1 = x2

else:
    print("\nmaximum iterations reached.")
    print("approximate root = %.6f" % x2)