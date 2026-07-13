import random
import time

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


