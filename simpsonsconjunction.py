# Simpson's Rules (1/3, 3/8, and Conjunction Method)

# input
f_str = input("Enter function f(x): ")

def f(x):
    return eval(f_str)

a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of segments (n): "))

# validation
if n < 2:
    print("n must be at least 2 for Simpson rules.")
    exit()

# step size
h = (b - a) / n

# x and y values
x = []
y = []

for i in range(n + 1):
    xi = a + i * h
    x.append(xi)
    y.append(f(xi))

# simpson's 1/3 rule
if n % 2 == 0:

    print("Applying Simpson's 1/3 Rule...")

    sum_odd = 0
    sum_even = 0

    for i in range(1, n):
        if i % 2 == 0:
            sum_even = sum_even + y[i]
        else:
            sum_odd = sum_odd + y[i]

    I = (h / 3) * (y[0] + 4 * sum_odd + 2 * sum_even + y[n])

# simpson's 3/8 rule
elif n % 3 == 0:

    print("Applying Simpson's 3/8 Rule...")

    sum1 = 0
    sum2 = 0

    for i in range(1, n):

        if i % 3 == 0:
            sum2 = sum2 + y[i]
        else:
            sum1 = sum1 + y[i]

    I = (3 * h / 8) * (y[0] + y[n] + 3 * sum1 + 2 * sum2)

# conjunction method
else:

    print("Applying Conjunction of 1/3 and 3/8 Rules...")

    # 1/3 rule for first 2 segments
    I1 = (h / 3) * (y[0] + 4 * y[1] + y[2])

    # remaining values
    y_rem = y[2:]
    n_rem = n - 2

    sum1 = 0
    sum2 = 0

    for i in range(1, n_rem):

        if i % 3 == 0:
            sum2 = sum2 + y_rem[i]
        else:
            sum1 = sum1 + y_rem[i]

    I2 = (3 * h / 8) * (y_rem[0] + y_rem[-1] + 3 * sum1 + 2 * sum2)

    I = I1 + I2

# output
print("Number of segments (n):", n)
print("Approximate Integral =", round(I, 8))