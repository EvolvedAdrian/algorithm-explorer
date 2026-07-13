from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.selection_sort import selection_sort
from algorithms.searching.binary_search import binary_search
from algorithms.searching.binary_search_recursive import binary_search_recursive
from algorithms.searching.linear_search import linear_search
from benchmark import get_test_arrays, benchmark_algorithm, format_time

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