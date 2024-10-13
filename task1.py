import timeit
import random

from sort_algs.insert import insertion_sort
from sort_algs.merge import merge_sort
from sort_algs.timsort import timsort


def time_algorithm(algorithm, arr):
    return timeit.timeit(lambda: algorithm(arr.copy()), number=1)

def generate_data(size):
    return [random.randint(0, 100000) for _ in range(size)]


def main():
    sizes = [1000, 5000, 10000]

    for size in sizes:
        data = generate_data(size)

        insertion_sort_time = time_algorithm(insertion_sort, data)
        merge_sort_time = time_algorithm(merge_sort, data)
        timsort_time = time_algorithm(timsort, data)

        print(f"For array of size: {size}:")
        print(f"Insertion Sort: {insertion_sort_time:.5f} sec")
        print(f"Merge Sort: {merge_sort_time:.5f} sec")
        print(f"Timsort (sorted): {timsort_time:.5f} sec")
        print("-" * 40)

if __name__ == "__main__":
    main()