# Jacobi Iterative Method with User Input

import numpy as np

# Inputs
A = np.array(eval(input("Enter coefficient matrix A (e.g., [[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]]): ")), dtype=float)
b = np.array(eval(input("Enter right-hand side vector b (e.g., [6,25,-11,15]): ")), dtype=float)
x0 = np.array(eval(input(f"Enter initial guess vector x0 of size {len(b)} (e.g., [0,0,0,0]): ")), dtype=float)
tol = float(input("Enter tolerance (e.g., 1e-6): "))
max_iter = int(input("Enter maximum number of iterations (e.g., 100): "))

n = len(b)

# Initialization
x_old = x0.copy()
x_new = np.zeros(n)

print("\nIteration\t", end="")
for i in range(n):
    print(f"x{i+1}\t\t", end="")
print("Abs Error\t\tRel Error")

# Jacobi Method
for k in range(1, max_iter + 1):
    for i in range(n):
        sum_ = 0
        for j in range(n):
            if j != i:
                sum_ += A[i, j] * x_old[j]
        x_new[i] = (b[i] - sum_) / A[i, i]
    
    # Error Calculation 
    abs_error = np.linalg.norm(x_new - x_old, ord=np.inf)
    rel_error = abs_error / (np.linalg.norm(x_new, ord=np.inf) + 1e-12)
    
    # Output
    print(f"{k}\t\t", end="")
    for xi in x_new:
        print(f"{xi:.6f}\t", end="")
    print(f"{abs_error:.2e}\t{rel_error:.2e}")
    
    if abs_error < tol:
        print(f"\nSolution converged in {k} iterations.")
        print("Solution vector X:")
        for i, xi in enumerate(x_new):
            print(f"x{i+1} = {xi:.6f}")
        break
    
    x_old = x_new.copy()
else:
    print("\nMaximum iterations reached without convergence.")