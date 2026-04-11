# Crout's LU Decomposition 

import numpy as np

# Inputs
A = np.array(eval(input("Enter coefficient matrix A (e.g., [[1,7,-4],[4,-4,9],[12,-1,3]]): ")))
B = np.array(eval(input("Enter constant vector B (e.g., [-51,62,8]): ")))
n = len(B)

# Initialization
L = np.zeros((n, n))
U = np.eye(n)  # Upper triangular with 1s on diagonal

# Crout's Decomposition
for j in range(n):
    # Compute L matrix
    for i in range(j, n):
        sum_ = 0
        for k in range(j):
            sum_ += L[i, k] * U[k, j]
        L[i, j] = A[i, j] - sum_
    
    # Compute U matrix
    for i in range(j + 1, n):
        sum_ = 0
        for k in range(j):
            sum_ += L[j, k] * U[k, i]
        U[j, i] = (A[j, i] - sum_) / L[j, j]

# Forward substitution: L * Y = B
Y = np.zeros(n)
for i in range(n):
    sum_ = 0
    for j in range(i):
        sum_ += L[i, j] * Y[j]
    Y[i] = (B[i] - sum_) / L[i, i]

# Back substitution: U * X = Y
X = np.zeros(n)
for i in range(n - 1, -1, -1):
    sum_ = 0
    for j in range(i + 1, n):
        sum_ += U[i, j] * X[j]
    X[i] = Y[i] - sum_

# Output
print("\nMatrix L:")
print(np.round(L, 6))

print("\nMatrix U:")
print(np.round(U, 6))

print("\nSolution X:")
for i in range(n):
    print(f"x{i+1} = {X[i]:.6f}")