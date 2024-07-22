import numpy as np 

def compute_vector_length1(vector):
    norm = np.sqrt(np.sum([v ** 2 for v in vector]))
    return norm

vector = np.array([-2, 4, 9, 21])
result = compute_vector_length1([vector])
print(round(result, 2))


def compute_vector_length2(vector):
    len_of_vector = np.linalg.norm(vector)

    return len_of_vector

vector2 = np.array([5, 9, -2, -1])
result = compute_vector_length2([vector2])
print(round(result, 2))