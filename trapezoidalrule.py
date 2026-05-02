# Trapezoidal Rule 

from scipy.integrate import quad

# USER INPUT 
f_str = input("Enter function f(x): ")

def f(x):
    return eval(f_str)

a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of intervals n: "))

# STEP SIZE 
h = (b - a) / n

# TRAPEZOIDAL RULE
sum_val = f(a) + f(b)

for i in range(1, n):
    x = a + i * h
    sum_val = sum_val + 2 * f(x)

I_trap = (h / 2) * sum_val

# -------- TRUE VALUE --------
I_true, _ = quad(lambda x: eval(f_str), a, b)

# -------- ERROR ANALYSIS --------
abs_error = abs(I_true - I_trap)
rel_error = abs_error / abs(I_true)

# -------- OUTPUT 
print("Trapezoidal Approximation =", round(I_trap, 6))
print("True Value               =", round(I_true, 6))
print("Absolute Error           =", format(abs_error, ".6e"))
print("Relative Error           =", format(rel_error, ".6e"))