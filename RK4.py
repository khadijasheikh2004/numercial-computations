# Runge-Kutta 4th Order Method (RK4)

import math
import matplotlib.pyplot as plt

# input
f_str = input("Enter the function f(t,y): ")

def f(t, y):
    return eval(f_str)

a = float(input("Enter the starting time (a): "))
b = float(input("Enter the ending time (b): "))
N = int(input("Enter the number of steps (N): "))
w = float(input("Enter the initial condition y(a): "))

# initialization
h = (b - a) / N
t = a

# lists to store values
t_out = []
w_out = []

# store initial values
t_out.append(t)
w_out.append(w)

# RK4 loop
for i in range(1, N + 1):

    K1 = h * f(t, w)

    K2 = h * f(t + h/2, w + K1/2)

    K3 = h * f(t + h/2, w + K2/2)

    K4 = h * f(t + h, w + K3)

    w = w + (K1 + 2*K2 + 2*K3 + K4) / 6

    t = a + i * h

    t_out.append(t)
    w_out.append(w)

# output
print("t\t w (approx)")

for i in range(len(t_out)):
    print(round(t_out[i], 4), "\t", round(w_out[i], 6))

# plot
plt.plot(t_out, w_out, marker='o')

plt.xlabel("t")
plt.ylabel("w (Approximation of y)")
plt.title("Runge-Kutta 4th Order (RK4) Approximation")

plt.grid(True)

plt.show()