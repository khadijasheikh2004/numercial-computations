# Simpson's 1/3 Rule 

from scipy.integrate import quad

# user input
f_str = input("Enter function f(x): ")

def f(x):
    return eval(f_str)

a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of intervals n: "))

# validation
if n % 2 != 0:
    print("Error: n must be even for Simpson's 1/3 Rule")
    exit()

# step size
h = (b - a) / n

# initial sum
sum_val = f(a) + f(b)

# simpsons loop
for i in range(1, n):
    x = a + i * h
    
    if i % 2 == 0:
        sum_val = sum_val + 2 * f(x)
    else:
        sum_val = sum_val + 4 * f(x)

# approximate value
I_simp = (h / 3) * sum_val

# true value
I_true, _ = quad(lambda x: eval(f_str), a, b)

# error analysis
abs_error = abs(I_true - I_simp)
rel_error = abs_error / abs(I_true)

# output
print("Simpson 1/3 Approximation =", round(I_simp, 6))
print("True Value               =", round(I_true, 6))
print("Absolute Error           =", format(abs_error, ".6e"))
print("Relative Error           =", format(rel_error, ".6e"))