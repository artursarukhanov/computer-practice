import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        max_el = abs(A[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > max_el:
                max_el = abs(A[k][i])
                max_row = k
        
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
            b[k] += c * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= A[k][i] * x[i]

    return x

def inverse_matrix_method(A, b):
    A_inv = np.linalg.inv(A)
    return np.dot(A_inv, b)

A = np.array([
    [-5, -6, 4, -2],
    [0, 3, -4, -6],
    [2, 4, -4, 2],
    [1, -8, 2, 8]
], dtype=float)

b = np.array([64, -55, -48, 68], dtype=float)

gauss_solution = gauss_elimination(A.copy(), b.copy())
print("Solution using Gauss Elimination:")
print(gauss_solution)

inverse_matrix_solution = inverse_matrix_method(A, b)
print("Solution using Inverse Matrix Method:")
print(inverse_matrix_solution)
