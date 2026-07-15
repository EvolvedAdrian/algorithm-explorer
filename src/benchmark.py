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

ARRAY_SIZES = [50, 500, 2000, 7000, 15000]
TEST_NUMS = [10, 20, 30, 40]
TIME_UNITS = ("s", "ms", "µs", "ns")


def generate_test_arrays():
    """ Defines a list of tests lists of different sizes for some algorithms benchmark.

    Returns:
        list[list]: List of test lists.
    """
    test_arrays = []
    for size in ARRAY_SIZES:
        test_arrays.append([random.randint(0,10) for _ in range(size)])
    
    return test_arrays

def benchmark_algorithm(algorithm, *args):
    """ Measure the execution time of a callable.

    Args:
        algorithm (callable): Function to benchmark.
        *args (tuple): Parameters of the function.

    Returns:
        float: Execution time

    Raises:
        RecursionError: If the function exceeds the maximum recursion depth.
    """
    start = time.perf_counter()
    algorithm(*args)
    end = time.perf_counter()
    return end - start

def format_time(num):
    """ Converts a time in seconds to a human-readable format. 

    Args:
        num (float): Time in seconds to convert.

    Returns:
        str: Time formated.
    """
    unit_index = 0

    while num < 1 and unit_index < len(TIME_UNITS):
        num*=1000
        unit_index+=1

    return f"{round(num, 2)} {TIME_UNITS[unit_index]}"

def print_benchmark_header(title):
    print("="*50)
    print(f"\n{title} BENCHMARK")
    print("="*50)

def launch_benchmark(algorithms_list, *args):
    for name, algorithm in algorithms_list:
        copied_args = [
            arg.copy() if isinstance(arg, list) else arg 
            for arg in args
            ]
        try:
            benchmark_result = format_time(benchmark_algorithm(algorithm, *copied_args))
        except RecursionError:
            benchmark_result = "ERROR: Maximum recursion depth exceeded."
        print(f"{name.capitalize():<20}{benchmark_result}")

def prepare_sorting_benchmark():
    test_arrays = generate_test_arrays()
    algorithms_list = [
        ("bubble sort", bubble_sort),
        ("insertion sort", insertion_sort),
        ("selection sort", selection_sort),
        ("merge sort", merge_sort),
        ("quick sort", quick_sort)
    ]

    print_benchmark_header("SORTING")

    for test_array in test_arrays:
        print(f"\nList size: {len(test_array)}\n")
        print(f"{'Algorithm':<20}Time")
        print("-"*30)

        launch_benchmark(algorithms_list, test_array)
        
def prepare_searching_benchmark():
    test_arrays = generate_test_arrays()
    numbers_to_find = [random.randint(0,9) for _ in range(len(test_arrays))]
    algorithms_list = [
        ("binary_search", binary_search),
        ("binary_search_recursive", binary_search_recursive),
        ("linear_search", linear_search)
    ]

    print_benchmark_header("SEARCHING")

    for test_array, number_to_find in zip(test_arrays, numbers_to_find):
        sorted_array = sorted(test_array)
        print(f"\nList size: {len(test_array)} Number to find: {number_to_find}\n")
        print(f"{'Algorithm':<20}Time")
        print("-"*30)

        launch_benchmark(algorithms_list, sorted_array, number_to_find)

def prepare_mathematics_benchmark():
    algorithms_list = [
        ("factorial", factorial_recursive),
        ("fibonacci_cached", fibonacci_cached),
        ("fibonacci_recursive", fibonacci_recursive)
    ]

    print_benchmark_header("MATHEMATICS")

    for test_num in TEST_NUMS:
        print(f"\nNumber: {test_num}\n")
        print(f"{'Algorithm':<20}Time")
        print("-"*30)

        launch_benchmark(algorithms_list, test_num)
