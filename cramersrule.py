import numpy as np

# Input
A = np.array(eval(input("Enter coefficient matrix A (e.g., [[2,-1],[1,3]]): ")))
B = np.array(eval(input("Enter constant vector B (e.g., [3,5]): ")))

n = len(B)

# Determinant of A
D = np.linalg.det(A)

if D == 0:
    print("The system has no unique solution")
else:
    X = np.zeros(n)

    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = B   # replace column

        X[i] = np.linalg.det(Ai) / D

    print("\nSolution:")
    for i in range(n):
        print(f"x{i+1} = {X[i]:.6f}")