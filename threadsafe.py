import threading
from concurrent.futures import ThreadPoolExecutor, wait

class ThreadSafeCounter:
    lock = threading.Lock()
    def __init__(self):
        self.count = 0
    def increment(self):
        with self.lock:
            self.count = self.count + 1

def count_up(counter):
    for _ in range(10000):
        counter.increment()

counter = ThreadSafeCounter()
threads = 2

with ThreadPoolExecutor() as e:
    futures = [e.submit(count_up, counter) for _ in range(threads)]
    done, not_done = wait(futures)

print(f'counter.count = {counter.count}')
