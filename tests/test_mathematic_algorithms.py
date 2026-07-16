import unittest
from src.algorithms.mathematics.factorial_recursive import factorial_recursive
from src.algorithms.mathematics.fibonacci_cached import fibonacci_cached
from src.algorithms.mathematics.fibonacci_recursive import fibonacci_recursive

class TestMathematicAlgorithms(unittest.TestCase):
    def setUp(self):
        self.algorithms_list = [factorial_recursive, fibonacci_cached, fibonacci_recursive]
        self.fibonacci_list = [fibonacci_cached, fibonacci_recursive]

    def test_factorial_base_case_0(self):
        self.assertEqual(factorial_recursive(0), 1)
    
    def test_factorial_number_1(self):
        self.assertEqual(factorial_recursive(1), 1)

    def test_factorial_normal_number(self):
        self.assertEqual(factorial_recursive(5), 120)

    def test_factorial_big_number(self):
        self.assertEqual(factorial_recursive(15), 1307674368000)
    
    def test_fibonacci_base_case_0(self):
        for algorithm in self.fibonacci_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm(0), 0)
    
    def test_fibonacci_base_case_1(self):
        for algorithm in self.fibonacci_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm(1), 1)

    def test_fibonacci_normal_number(self):
        for algorithm in self.fibonacci_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm(6), 8)

    def test_fibonacci_big_number(self):
        for algorithm in self.fibonacci_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm(20), 6765)
    
    def test_negative_number_raises_value_error(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                with self.assertRaises(ValueError):
                    algorithm(-1)
