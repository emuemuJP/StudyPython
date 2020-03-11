import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
def elapsed_time(f):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}: {time.time() - st}")
        return v
    return wrapper

def fibonacchi(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b + a
    else:
        return a

@elapsed_time
def main(n):
    fibonacchi(n)

@elapsed_time
def get_sequential(nums):
    for num in nums:
        fibonacchi(num)

@elapsed_time
def get_multi_process(num):
    with ProcessPoolExecutor() as e:
        futures = [e.submit(fibonacchi, num) for num in nums]
        for future in as_completed(futures):
            future.result()

@elapsed_time
def get_thread_process(num):
    with ThreadPoolExecutor() as e:
        futures = [e.submit(fibonacchi, num) for num in nums]
        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    n = int(sys.argv[1])
    nums = [n] * os.cpu_count()
    main(n)
    get_sequential(nums)
    get_thread_process(nums)
    get_multi_process(nums)