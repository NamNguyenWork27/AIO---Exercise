import numpy as np 
def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

m1 = np.matrix([[0, 1, 2], [2, -3, 1]])
m2 = np.matrix([[1, -3], [6, 1], [0, -1]])
result = matrix_multi_matrix(m1, m2)
print(result)

