import time
from contextlib import contextmanager

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, *args):
        print(time.perf_counter() - self.start)

@contextmanager
def timer():
    start = time.perf_counter()
    yield
    print(time.perf_counter() - start)

with Timer():
    sum(range(1000000))

with timer():
    sum(range(1000000))
