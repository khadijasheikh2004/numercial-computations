# Newton Raphson Method 

import math

# input function
f_str = input("enter function f(x): ")

# input derivative
df_str = input("enter derivative f'(x): ")

# convert string to functions
def f(x):
    return eval(f_str)

def df(x):
    return eval(df_str)

# take inputs
x0 = float(input("enter initial guess: "))
tol = float(input("enter tolerance: "))
max_iter = int(input("enter maximum iterations: "))

# header
print("\niter\t x\t\t f(x)\t\t error(%)")

for i in range(1, max_iter + 1):
    fx = f(x0)
    dfx = df(x0)

    # Newton Raphson formula
    x1 = x0 - fx/dfx

    # relative error
    error = abs((x1 - x0) / x1) * 100

    print("%d\t %.6f\t %.6f\t %.6f" % (i, x1, f(x1), error))

    # stopping condition
    if abs(x1 - x0) < tol:
        print("\nconverged.")
        print("approximate root = %.6f" % x1)
        print("number of iterations =", i)
        break

    x0 = x1

else:
    print("\nmaximum iterations reached.")
    print("approximate root = %.6f" % x1)