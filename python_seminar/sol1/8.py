import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        print(time.perf_counter() - start)
        return res
    return wrapper

@measure_time
def f(n):
    return sum(range(n))

print(f(1000000))
