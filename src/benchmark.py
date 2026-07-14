from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.selection_sort import selection_sort
from algorithms.searching.binary_search import binary_search
from algorithms.searching.binary_search_recursive import binary_search_recursive
from algorithms.searching.linear_search import linear_search
from algorithms.mathematics.factorial_recursive import factorial_recursive
from algorithms.mathematics.fibonacci_recursive import fibonacci_recursive
from algorithms.mathematics.fibonacci_cached import fibonacci_cached
import random
import time

def get_test_arrays():
    array_sizes = [50, 500, 2000, 7000, 15000]
    test_arrays = []
    for size in array_sizes:
        test_arrays.append([random.randint(0,10) for _ in range(size)])
    
    return test_arrays

def benchmark_algorithm(algorithm, *args):
    try:
        start = time.perf_counter()
        algorithm(*args)
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

def print_benchmark_header(title):
    print("="*50)
    print(f"\n{title} BENCHMARK")
    print("="*50)

def prepare_sorting_benchmark():
    test_arrays = get_test_arrays()
    algorithms_list = [
        ("bubble sort", bubble_sort),
        ("insertion sort", insertion_sort),
        ("selection sort", selection_sort),
        ("merge sort", merge_sort),
        ("quick sort", quick_sort)
    ]

    print_benchmark_header("SORTING")
    launch_sorting_benchmark(test_arrays, algorithms_list)

def prepare_searching_benchmark():
    test_arrays = get_test_arrays()
    numbers_to_find = [random.randint(0,9) for _ in range(len(test_arrays))]
    algorithms_list = [
        ("binary_search", binary_search),
        ("binary_search_recursive", binary_search_recursive),
        ("linear_search", linear_search)
    ]

    print_benchmark_header("SEARCHING")
    launch_searching_benchmark(test_arrays, algorithms_list, numbers_to_find)

def prepare_mathematics_benchmark():
    test_nums = [10, 20, 30, 40]
    algorithms_list = [
        ("factorial", factorial_recursive),
        ("fibonacci_cached", fibonacci_cached),
        ("fibonacci_recursive", fibonacci_recursive)
    ]

    print_benchmark_header("MATHEMATICS")
    launch_mathematics_benchmark(test_nums, algorithms_list)

def launch_sorting_benchmark(test_arrays, algorithm_list):
    for test_array in test_arrays:
        print(f"\nList size: {len(test_array)}\n")
        print(f"{'Algorithm':<20}Time")
        print("-"*30)

        for name, algorithm in algorithm_list:
            benchmark_result = benchmark_algorithm(algorithm, test_array.copy())
            if not isinstance(benchmark_result, str): benchmark_result = format_time(benchmark_result)
            print(f"{name.capitalize():<20}{benchmark_result}")

def launch_searching_benchmark(test_arrays, algorithm_list, numbers_to_find):
    for test_array, number_to_find in zip(test_arrays, numbers_to_find):
        sorted_array = sorted(test_array)
        print(f"\nList size: {len(test_array)} | Number to find: {number_to_find}\n")
        print(f"{'Algorithm':<20}Time")
        print("-"*30)

        for name, algorithm in algorithm_list:
            benchmark_result = benchmark_algorithm(algorithm, sorted_array, number_to_find)
            if not isinstance(benchmark_result, str): benchmark_result = format_time(benchmark_result)
            print(f"{name.capitalize():<20}{benchmark_result}")

def launch_mathematics_benchmark(test_nums, algorithm_list):
    for test_num in test_nums:
        print(f"\nNumber: {test_num}\n")
        print(f"{'Algorithm':<20}Time")
        print("-"*30)

        for name, algorithm in algorithm_list:
            benchmark_result = benchmark_algorithm(algorithm, test_num)
            if not isinstance(benchmark_result, str): benchmark_result = format_time(benchmark_result)
            print(f"{name.capitalize():<20}{benchmark_result}")

