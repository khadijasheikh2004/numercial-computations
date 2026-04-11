# Gauss Elimination Method

# n = int(input("Enter number of variables: "))

# # Input matrix A
# A = []
# print("Enter matrix A row-wise:")
# for i in range(n):
#     A.append(list(map(float, input().split())))

# # Input vector b
# b = list(map(float, input("Enter vector b: ").split()))

# # Forward Elimination 
# for k in range(n):
#     # Pivot check
#     if A[k][k] == 0:
#         print("Zero pivot encountered!")
#         exit()

#     for i in range(k+1, n):
#         factor = A[i][k] / A[k][k]
#         for j in range(k, n):
#             A[i][j] -= factor * A[k][j]
#         b[i] -= factor * b[k]

# # Back Substitution 
# x = [0]*n

# for i in range(n-1, -1, -1):
#     sum_ax = 0
#     for j in range(i+1, n):
#         sum_ax += A[i][j] * x[j]
#     x[i] = (b[i] - sum_ax) / A[i][i]

# # Output 
# print("\nSolution:")
# for i in range(n):
#     print(f"x{i+1} = {x[i]:.6f}")

# Gaussian Elimination

import numpy as np

# Input Section 
A = np.array(eval(input("Enter coefficient matrix A (e.g., [[2,1],[5,7]]): ")))
B = np.array(eval(input("Enter constant vector B (e.g., [11,13]): ")))

# Initialization 
n = len(B)
Aug = np.hstack((A, B.reshape(-1, 1)))  # Form augmented matrix
x = np.zeros(n)                          # Solution vector

# Core Algorithm 
# Forward Elimination
for i in range(n - 1):
    for j in range(i + 1, n):
        factor = Aug[j, i] / Aug[i, i]
        Aug[j, :] = Aug[j, :] - factor * Aug[i, :]

# Back Substitution
x[n - 1] = Aug[n - 1, n] / Aug[n - 1, n - 1]

for i in range(n - 2, -1, -1):
    sum_ = 0
    for j in range(i + 1, n):
        sum_ += Aug[i, j] * x[j]
    x[i] = (Aug[i, n] - sum_) / Aug[i, i]

# Output
print("\nSolution of the system is:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.6f}")