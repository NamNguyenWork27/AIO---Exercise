import numpy as np 

def compute_eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    return eigenvalues, eigenvectors

input_matrix = np.array([[0, 1], [-2, 5]])
print(input_matrix.shape)
eigenvalue, eigenvector = compute_eigen(input_matrix)
print(eigenvalue)
print(eigenvector)