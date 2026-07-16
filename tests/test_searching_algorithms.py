import unittest
from src.algorithms.searching.linear_search import linear_search
from src.algorithms.searching.binary_search import binary_search
from src.algorithms.searching.binary_search_recursive import binary_search_recursive

class TestSearchingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.algorithms_list = [linear_search, binary_search, binary_search_recursive]
        self.binary_search_list = [binary_search, binary_search_recursive]

    def test_empty_list(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([], 5), -1)
    
    def test_one_element_list_non_exists(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([5], 0), -1)

    def test_one_element_list_exists(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([5], 5), 0)
    
    def test_search_first(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([1,2,3,4,5], 1), 0)

    def test_search_last(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([1,2,3,4,5], 5), 4)

    def test_equal_elements_list_non_exists(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([7,7,7,7,7], -7), -1)
    
    def test_equal_elements_list_exists(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertIn(algorithm([7,7,7,7,7], 7), (0,1,2,3,4))
    
    def test_repeated_elements_unordered_list_non_exists(self):   
        self.assertEqual(linear_search([5,1,4,0,1,4,2], 10), -1)
    
    def test_repeated_elements_unordered_list_exists(self):
        self.assertEqual(linear_search([5,1,4,0,1,4,2], 1), 1)
    
    def test_negative_numbers_unordered_list_non_exists(self):
        self.assertEqual(linear_search([-8,3,-2,10,0,-5], -1), -1)
    
    def test_negative_numbers_unordered_list_exists(self):
        self.assertEqual(linear_search([-8,3,-2,10,0,-5], -5), 5)
    
    def test_repeated_elements_ordered_list_non_exists(self):
        for algorithm in self.binary_search_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([1,2,2,2,3,4], 5), -1)
    
    def test_repeated_elements_ordered_list_exists(self):
        for algorithm in self.binary_search_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertIn(algorithm([1,2,2,2,3,4], 2), (1,2,3))

    def test_negative_elements_ordered_list_non_exists(self):
        for algorithm in self.binary_search_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([-4,-3,-2,0,1,2,2], -1), -1)
    
    def test_negative_elements_ordered_list_exists(self):
        for algorithm in self.binary_search_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([-4,-3,-2,-1,0,1,2,2], -1), 3)
    
    def test_two_elements_ordered_list_exists_first(self):
        for algorithm in self.binary_search_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([1,2], 1), 0)

    def test_two_elements_ordered_list_exists_second(self):
        for algorithm in self.binary_search_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([1,2], 2), 1)

    def test_two_elements_ordered_list_non_exists(self):
        for algorithm in self.binary_search_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([1,2], 3), -1)

