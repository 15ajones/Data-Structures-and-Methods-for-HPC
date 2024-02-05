import pytest
import numpy as np
import sys
from timeit import default_timer as timer

def test_dgemm():
    N = 1
    C = np.zeros((N, N))
    A = np.zeros((N, N))
    B = np.zeros((N, N))

    A[0][0] = 2.0
    B[0][0] = 4.0
    C[0][0] = 1.0
    Ans1 = dgemm_matmul(A, B, C, N)[0][0]
    A[0][0] = 2.0
    B[0][0] = 4.0
    C[0][0] = 1.0
    Ans2 = dgemm_matmul(B, A, C, N)[0][0]
    A[0][0] = 2.0
    B[0][0] = 4.0
    C[0][0] = 1.0
    Ans3 = dgemm_matmul(A, A, C, N)[0][0]
    A[0][0] = 2.0
    B[0][0] = 4.0
    C[0][0] = 1.0
    Ans4 = dgemm_matmul(C, C, C, N)[0][0]

    A[0][0] = 2.0
    B[0][0] = 4.0
    C[0][0] = 1.0
    assert(Ans1 == dgemm(A, B, C, N)[0][0])
    A[0][0] = 2.0
    B[0][0] = 4.0
    C[0][0] = 1.0
    assert(Ans2 == dgemm(B, A, C, N)[0][0])
    A[0][0] = 2.0
    B[0][0] = 4.0
    C[0][0] = 1.0
    assert(Ans3 == dgemm(A, A, C, N)[0][0])
    A[0][0] = 2.0
    B[0][0] = 4.0
    C[0][0] = 1.0
    assert(Ans4 == dgemm(C, C, C, N)[0][0])

# DGEMM naive
def dgemm(A, B, C, N):
    for i in range(0, N):
        for j in range(0, N):
            for k in range(0, N):
                C[i][j] = C[i][j] + (A[i][k] * B[k][j])
    return C

# DGEMM matmul
def dgemm_matmul(A, B, C, N):
    C += np.matmul(A, B)
    print(C)
    return C

N = 1# = int(sys.argv[1])
n = 1# int(sys.argv[2])

times = []
times_matmul = []
for i in range(n):
    C = np.zeros((N, N))
    A = np.zeros((N, N))
    B = np.zeros((N, N))
    times.append(timer())
    dgemm(A, B, C, N)
    times[i] = timer() - times[i]
    times_matmul.append(timer())
    dgemm_matmul(A, B, C, N)
    times_matmul[i] = timer() - times_matmul[i]
print("Naive: avg = ", np.mean(times), " std = ", np.std(times))
print("BLAS: avg = ", np.mean(times_matmul), " std = ", np.std(times_matmul))
print("Speedup factor: ", (np.mean(times) / np.mean(times_matmul)))