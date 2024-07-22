import numpy as np 
def compute_cosine_sim(v1, v2):
    result = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return result

v1 = np.array([1000, 10, -1000])
v2 = np.array([1, 2, 3])
result = compute_cosine_sim(v1, v2)
print(result)

