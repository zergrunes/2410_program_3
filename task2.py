'''Marian Remoroza
CS 2410 Data Science
Program 3'''
import numpy as np
import numpy.matlib
import sys
# solving system of linear equations
# x+y+z = 6
# x+2y+2z = 11
# 2x+3y-4z = 3
a = np.array([[1, 1, 1], [1, 2, 2], [2, 3, -4]])
b = np.array([6, 11, 3])
ans = np.linalg.solve(a, b)
print("Answer:", ans)

''' 
w+2x-y+z=6
-w+x+2y-z=3
2w-x+2y+2z=14
w+x-y+2z=8'''

c = np.array([[1, 2, -1, 1], [-1, 1, 2, -1], [2, -1, 2, 2], [1, 1, -1, 2]])
d = np.array([6, 3, 14, 8])
ans2 = np.linalg.solve(c, d)
print("\nAnswer:", ans2)
