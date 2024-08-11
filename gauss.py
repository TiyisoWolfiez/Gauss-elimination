import numpy as np
import random
def gauss(A,b):
    n = len(A)
    A = np.hstack((A,b))
# Elimination process
    for i in range(0,n-1):
        # step 2
        p = i        
        while p <= n and A[p][i] == 0:
            p = p + 1
        if p == n+1:
            raise ValueError("Matrix A is singular")
        # step 3 
        if p != i:
            A[[i,p]] = A[[p,i]]
        # step 4, do steps 5 and 6    
        for j in range(i+1,n):
            m = A[j][i]/A[i][i]
            for k in range(i,n+1):
                A[j][k] = A[j][k] - m*A[i][k]        
    # step 7                            
    if A[n-1][n-1] == 0:
        raise ValueError("Matrix A is singular")        
# back substitution process
    # Back substitution process
    x = np.zeros(n)
    # Step 8
    x[n-1] = A[n-1][n] / A[n-1][n-1]
    # Step 9
    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += A[i][j] * x[j]
        x[i] = (A[i][n] - sum_ax) / A[i][i]

    # Step 10: Output the solution vector
    return x

    
def main():
    # Example system: 2x + 3y + z = 1
    #                 4x + y + 2z = 2
    #                 3x + 2y + 3z = 3
    
    A = np.array([[1, 1, 0, 3],
                  [2, 1, -1, 1],
                  [3, -1, -1, 2],
                  [-1, 2 , 3 , -1]], dtype=float)
    
    b = np.array([[4], 
                  [1], 
                  [-3],
                  [4]], dtype=float)
    
    # try:
    # solution = gauss(A, b)
    # print("Solution vector x:", solution)
    print("Solution vector x:", gauss(A, b))
    # except ValueError as e:
        # print(e)

# if __name__ == "__main__":
main()

