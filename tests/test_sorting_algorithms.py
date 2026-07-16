import unittest
from src.algorithms.sorting.bubble_sort import bubble_sort
from src.algorithms.sorting.insertion_sort import insertion_sort
from src.algorithms.sorting.selection_sort import selection_sort
from src.algorithms.sorting.merge_sort import merge_sort
from src.algorithms.sorting.quick_sort import quick_sort

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.algorithms_list = [bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort]

    def test_empty_list(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([]), [])
    
    def test_one_element_list(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([5]), [5])
    
    def test_two_elements_sorted_list(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([8,9]), [8,9])
    
    def test_two_elements_unsorted_list(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([9,8]), [9,8])
    
    def test_repeated_elements_list(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([5,1,4,0,1,4,2]), [0,1,1,2,4,4,5])
    
    def test_negative_numbers_list(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([-8,3,-2,10,0,-5]), [-8,-5,-2,0,3,10])

    def test_equal_elements_list(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([7,7,7,7,7]), [7,7,7,7,7])

    def test_inverse_sorted_list(self):
        for algorithm in self.algorithms_list:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([6,5,4,3,2,1,0]), [0,1,2,3,4,5,6])
