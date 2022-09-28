import random
import time

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def linear_search(array, x, *args):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1


def binary_search(array, x, left, right):
    if left >= right:
        return -1
    else:
        mid = (left + right) // 2
        if array[mid] == x:
            return mid
        elif x < array[mid]:
            return binary_search(array, x, left, mid)
        else:
            return binary_search(array, x, mid + 1, right)


def measure_algorithm(search, sample, target_value):
    times = []
    for step in range(100):
        start = time.perf_counter()
        search(sample, target_value, 0, len(sample))
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)


def main():
    random_left = 0
    random_right = 1000
    results = {"binary": [], "linear": []}
    sample_sizes = [100, 1000, 5000, 10000, 100000, 1000000, 10000000]

    for sample_size in sample_sizes:
        sample = [random.randint(random_left, random_right) for _ in
                  range(sample_size)]
        target_value = random.randint(random_left, random_right)
        linear_time = measure_algorithm(linear_search, sample, target_value)
        results["linear"].append(linear_time)
        binary_time = measure_algorithm(binary_search, sample, target_value)
        results["binary"].append(binary_time)

    # pprint.pprint(results)

    plt.plot(sample_sizes, results["linear"], label="linear", color="red")
    plt.plot(sample_sizes, results["binary"], label="binary", color="blue")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
