'''Marian Remoroza
CS 2410 Data Science
Program 3'''
import numpy as np
import numpy.matlib
import sys

'''Matrix-vector multiplication M x v'''
arr_m = np.array([[2, 1, 3, 1, -2, 1], [1, -3, -4, 10, 4, 2], [1, 2, 3, 4, 5, 6],
                 [2, 0, 2, 0, 3, 1], [1, 2, 3, 3, 2, 1], [5, 1, 6, 1, -7, -2]])
v = np.array([1, -4, 2, 2, 1, 8])
mv = np.matmul(arr_m, v)
print("Matrix-vector multiplication:\n", mv, "\n")
'''Matrix-matrix multiplication m1xm2'''
m1 = np.array([[2, 1, 3, 1, -2, 1], [1, -3, -4, 10, 4, 2],
              [1, 2, 3, 4, 5, 6], [2, 0, 2, 0, 3, 1], [1, 2, 3, 3, 2, 1]])
m2 = np.array([[2, 1, 3, 1], [1, -3, 4, 2], [3, 4, 5, 6],
              [2, 0, 2,  1], [1, 2, 2, 1], [5, 1, 1, -2]])
print("Matrix-matrix multiplication:\n", np.matmul(m1, m2), "\n")
'''Matrix transposition'''
m1_t = np.array([[2, 1, 3, 1], [1, -3, 4, 2], [3, 4, 5, 6],
                [2, 0, 2, 1], [1, 2, 2, 1], [5, 1, 1, -2]])
m2_t = m1_t.T
print("Matrix transposition:\n", m2_t, "\n")
'''Apply square root to each element of a matrix'''
m_sq = np.array([[2, 1, 4, 1, 9, 1],
                 [1, 36, 4, 10, 4, 2],
                 [1, 2, 3, 4, 5, 6],
                 [2, 0, 2, 0, 3, 1],
                 [1, 2, 3, 3, 2, 1],
                 [5, 1, 6, 1, 9, 25]])
m_sqrt = np.sqrt(m_sq)
print("Square root to each element of a matrix:\n",
      m_sqrt)  # this isn't printing out correctly
'''Adding up all elements in a matrix'''
madd = np.array([[2, 1, 3, 1, -2, 1], [1, -3, -4, 10, 4, 2], [1, 2, 3, 4, 5, 6],
                [2, 0, 2, 0, 3, 1], [1, 2, 3, 3, 2, 1], [5, 1, 6, 1, -7, -2]])
print("\nSum of all elements in a matrix:", np.sum(madd))
'''Perform a matrix operation of your choic'''
