import random
import time

_SIZE = int(10e+6)

max_value = -float("inf")
data = [random.randint(0, 100) for _ in range(_SIZE)]
start = time.perf_counter()
for item in data:
    if item > max_value:
        max_value = item
print(f"elapsed time: {(time.perf_counter() - start):.5f}")
