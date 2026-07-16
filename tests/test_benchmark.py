from src.benchmark import generate_test_arrays
from src.benchmark import format_time
from src.benchmark import benchmark_algorithm
from src.algorithms.sorting.bubble_sort import bubble_sort
from src.benchmark import ARRAY_SIZES
import unittest

class TestBenchmark(unittest.TestCase):
    def test_generate_test_arrays_length(self):
        test_arrays = generate_test_arrays()
        self.assertEqual(len(test_arrays), len(ARRAY_SIZES))
    
    def test_generate_test_arrays_array_lengths(self):
        test_arrays = generate_test_arrays()
        for test_arr, arr_size in zip(test_arrays, ARRAY_SIZES):
            self.assertEqual(len(test_arr), arr_size)

    def test_generate_test_arrays_internal_element_types(self):
        test_arrays = generate_test_arrays()
        for test_arr in test_arrays:
            for el in test_arr:
                self.assertIsInstance(el, int)

    def test_generate_test_arrays_value_limits(self):
        test_arrays = generate_test_arrays()
        for test_arr in test_arrays:
            for el in test_arr:
                self.assertGreaterEqual(el, 0)
                self.assertLessEqual(el, 10)

    def test_benchmark_algorithm_returns_float(self):
        self.assertIsInstance(benchmark_algorithm(bubble_sort, [6,4,2,1]), float)

    def test_benchmark_algorithm_returns_greater_than_0(self):
        self.assertGreaterEqual(benchmark_algorithm(bubble_sort, [6,4,2,1]), 0)
    
    def test_format_time_0(self):
        self.assertEqual(format_time(0), "0 s")

    def test_format_time_one_second(self):
        self.assertEqual(format_time(1), "1 s")
    
    def test_format_time_miliseconds(self):
        self.assertEqual(format_time(0.0345), "34.5 ms")

    def test_format_time_microseconds(self):
        self.assertEqual(format_time(0.00067), "670 µs")
    
    def test_format_time_nanoseconds(self):
        self.assertEqual(format_time(0.000000002), "2 ns")
    
    def test_format_time_big_time(self):
        self.assertEqual(format_time(700.4), "700.4 s")
    
    def test_format_time_low_time(self):
        self.assertEqual(format_time(0.00000000000250080), "0 ns")
