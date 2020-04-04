import numpy as np


## Used for Spring Model implementation only
def euclidean(v1: np.ndarray, v2: np.ndarray) -> float:
    return np.linalg.norm(v2 - v1)
