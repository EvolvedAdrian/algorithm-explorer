import random
import time
from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.selection_sort import selection_sort
from algorithms.searching.binary_search import binary_search
from algorithms.searching.binary_search_recursive import binary_search_recursive
from algorithms.searching.linear_search import linear_search

def get_test_arrays(arr_sizes):
    test_arrays = []
    for size in arr_sizes:
        test_arrays.append([random.randint(0,10) for _ in range(size)])
    
    return test_arrays

def benchmark_algorithm(algorithm, test_array):
    try:
        start = time.perf_counter()
        algorithm(test_array)
        end = time.perf_counter()
        return end - start
    except RecursionError:
        return "ERROR: Max recursion depth exceeded"

def format_time(num):
    unit_index_counter = 0
    unit_list = ["s", "ms", "µs", "ns"]

    while num < 1 and unit_index_counter < len(unit_list):
        num*=1000
        unit_index_counter+=1

    return f"{round(num, 2)} {unit_list[unit_index_counter]}"

array_sizes = [50, 500, 2000, 7000, 15000]
test_arrays = get_test_arrays(array_sizes)
sorting_algorithms = [
    ("bubble sort", bubble_sort),
    ("insertion sort", insertion_sort),
    ("selection sort", selection_sort),
    ("merge sort", merge_sort),
    ("quick sort", quick_sort)
]
searching_algorithms = [binary_search, binary_search_recursive, linear_search]

print("="*50)
print("\nSORTING BENCHMARK --> Time measurement")
print("="*50)

for i, test_array in enumerate(test_arrays):
    print(f"\nArray size: {array_sizes[i]}\n")
    print(f"{'Algorithm':<20}Time")
    print("-"*30)

    for name, algorithm in sorting_algorithms:
        benchmark_result = benchmark_algorithm(algorithm, test_array.copy())
        if not isinstance(benchmark_result, str): benchmark_result = format_time(benchmark_result)
        print(f"{name.capitalize():<20}{benchmark_result}")
