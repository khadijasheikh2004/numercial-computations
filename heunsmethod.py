# Heun's Method 

import math

# input
f_str = input("Enter function dy/dx = f(x,y): ")

def f(x, y):
    return eval(f_str)

xi = float(input("Enter initial x value (xi): "))
xf = float(input("Enter final x value (xf): "))
y = float(input("Enter initial y value (y0): "))
h = float(input("Enter step size (h): "))

# initialization
x = xi
n = int((xf - xi) / h)

# table header
print("\n x\t    y")
print(round(x, 2), "\t", round(y, 6))

# heun's method loop
for i in range(n):

    slope1 = f(x, y)

    y_pred = y + slope1 * h

    x_next = x + h

    slope2 = f(x_next, y_pred)

    avg_slope = (slope1 + slope2) / 2

    y = y + avg_slope * h

    x = x_next

    print(round(x, 2), "\t", round(y, 6))