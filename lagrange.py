# Lagrange Interpolating Polynomial

import sympy as sp

# Input
x_data = list(map(float, input("Enter x values: ").split()))
y_data = list(map(float, input("Enter y values: ").split()))
x_val = float(input("Enter the value of x to evaluate the polynomial: "))

n = len(x_data)

# Initialization 
x = sp.symbols('x')
L_poly = 0

# Algorithm 
for i in range(n):
    Li = 1
    for j in range(n):
        if i != j:
            Li *= (x - x_data[j]) / (x_data[i] - x_data[j])
    L_poly += y_data[i] * Li

# Output 
L_poly_simplified = sp.simplify(L_poly)

print("\nInterpolating Polynomial:")
print(L_poly_simplified)

# Evaluate at given point
value = L_poly_simplified.subs(x, x_val)
print(f"\nValue of polynomial at x = {x_val} is: {float(value):.6f}")