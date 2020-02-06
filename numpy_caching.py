import numpy as np
import cachetools

def lru_cache_numpy(func):
    """ numpy friendly caching """
    maxsize = 128
    cache = cachetools.LRUCache(maxsize=maxsize)
    def hashing_first_numpy_arg(*args, **kwargs):
        """ sum up the hash of all the arguments """
        hash_total = 0
        for x in [*args, *kwargs.values()]:
            if isinstance(x,np.ndarray):
                hash_total += hash(x.data.tobytes() )
            else:
                hash_total += hash(x)                
        return hash_total
    return cachetools.cached(cache, hashing_first_numpy_arg)(func)

    
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


