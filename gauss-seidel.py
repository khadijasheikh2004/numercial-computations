# Gauss-Seidel Iterative Method 

import numpy as np

# Input
A = np.array(eval(input("Enter coefficient matrix A (e.g., [[10,1,1],[2,10,1],[2,2,10]]): ")), dtype=float)
b = np.array(eval(input("Enter right-hand side vector b (e.g., [12,13,14]): ")), dtype=float)
x0 = np.array(eval(input(f"Enter initial guess vector x0 of size {len(b)} (e.g., [0,0,0]): ")), dtype=float)
tol = float(input("Enter tolerance (e.g., 1e-6): "))
max_iter = int(input("Enter maximum iterations (e.g., 100): "))

n = len(b)

# Initialization
x = x0.copy()

print("\nIteration\t", end="")
for i in range(n):
    print(f"x{i+1}\t\t", end="")
print("Abs Error\t\tRel Error")

# Gauss-Seidel Iteration
for k in range(1, max_iter + 1):
    x_old = x.copy()
    
    for i in range(n):
        sum_ = 0
        for j in range(n):
            if j != i:
                sum_ += A[i, j] * x[j]  # Use latest x values
        x[i] = (b[i] - sum_) / A[i, i]
    
    # Error Calculation 
    abs_error = np.linalg.norm(x - x_old, ord=np.inf)
    rel_error = abs_error / (np.linalg.norm(x, ord=np.inf) + 1e-12)
    
    # Output 
    print(f"{k}\t\t", end="")
    for xi in x:
        print(f"{xi:.6f}\t", end="")
    print(f"{abs_error:.2e}\t{rel_error:.2e}")
    
    if abs_error < tol:
        print(f"\nSolution converged in {k} iterations")
        break

print("\nFinal Solution Vector X:")
for i, xi in enumerate(x):
    print(f"x{i+1} = {xi:.6f}")