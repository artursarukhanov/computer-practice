import numpy as np

def seidel_method(A, b, tolerance=1e-10, max_iterations=1000):
    n = len(b)
    x = np.zeros(n)
    
    for _ in range(max_iterations):
        x_new = np.copy(x)
        
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new
        
        x = x_new
    
    return x

A = np.array([
    [15, -4, -6, 5],
    [4, -14, -1, 4],
    [7, -7, 27, -8],
    [-3, -3, 2, -14]
], dtype=float)

b = np.array([104, 70, 170, 48], dtype=float)

solution = seidel_method(A, b)
print("Solution using Seidel Method:")
print(solution)
