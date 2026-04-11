# # Gauss-Jordan Method

# n = int(input("Enter number of variables: "))

# # Input matrix A
# A = []
# print("Enter matrix A row-wise:")
# for i in range(n):
#     A.append(list(map(float, input().split())))

# # Input vector b
# b = list(map(float, input("Enter vector b: ").split()))

# # Form augmented matrix
# for i in range(n):
#     A[i].append(b[i])

# # Gauss-Jordan Elimination 
# for i in range(n):
#     # Pivot check
#     if A[i][i] == 0:
#         print("Zero pivot encountered!")
#         exit()

#     # Make pivot = 1
#     pivot = A[i][i]
#     for j in range(n+1):
#         A[i][j] /= pivot

#     # Make other elements in column 0
#     for k in range(n):
#         if k != i:
#             factor = A[k][i]
#             for j in range(n+1):
#                 A[k][j] -= factor * A[i][j]

# # Extract solution 
# print("\nSolution:")
# for i in range(n):
#     print(f"x{i+1} = {A[i][n]:.6f}")

# Gauss-Jordan Elimination

import numpy as np

# Input Section
A = np.array(eval(input("Enter coefficient matrix A (e.g., [[2,1],[5,7]]): ")), dtype=float)
B = np.array(eval(input("Enter constant vector B (e.g., [11,13]): ")), dtype=float)

# Initialization
n = len(B)
Aug = np.hstack((A, B.reshape(-1, 1)))  # Form augmented matrix

# Core Algorithm 
for i in range(n):
    # Make pivot = 1
    Aug[i, :] = Aug[i, :] / Aug[i, i]
    
    # Make other elements in the column = 0
    for j in range(n):
        if j != i:
            factor = Aug[j, i]
            Aug[j, :] = Aug[j, :] - factor * Aug[i, :]

# Solution vector
x = Aug[:, n]

# Output 
print("\nReduced Row Echelon Form of Augmented Matrix:")
print(np.round(Aug, 6))

print("\nSolution of the system:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.6f}")