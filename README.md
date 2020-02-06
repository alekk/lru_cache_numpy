# lru_cache_numpy

''' python
from numpy_caching import lru_cache_numpy

@lru_cache_numpy
def func(A,B):
    result = np.sum(A**2)
    print("... computations.... ->", result)
    return result

A = np.random.normal(0,1, 3)
B = np.random.normal(0,1, 3)

print(func(A,B))
print(func(A,B+1))
print(func(A+1,B))
print(func(A,B))
'''
