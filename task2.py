import numpy as np
from sort_algs.merge import merge_sort

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

def merge_k_lists(arr):
    flattened = np.hstack(arr)
    sorted_arr = merge_sort(flattened.tolist())

    return sorted_arr

print(merge_k_lists(lists))