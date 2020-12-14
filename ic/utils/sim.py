import numpy as np


def cos_sim(a: np.ndarray, b: np.ndarray) -> np.float32:
    # cosine similarity
    return np.dot(a, b) / (np.linalg.norm(a)*np.linalg.norm(b))
