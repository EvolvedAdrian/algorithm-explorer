""" Sorts numbers in ascending order using bubble sort optimized algorithm.
It modifies the original list.

Args: elem_list (list)

Returns: tuple[list,int] --> (bubble sort ordered list, number of comparisons) 
"""
def bubble_sort(elem_list):
    # Optimizations
    array_sorted = False
    ordered_numbers = 0
    # Metrics
    n_comparisons = 0
    while not array_sorted:
        array_sorted = True
        for i in range(1, len(elem_list)-ordered_numbers):
            n_comparisons+=1
            if elem_list[i] < elem_list[i-1]:
                array_sorted = False
                elem_list[i], elem_list[i-1] = elem_list[i-1], elem_list[i]
        ordered_numbers+=1
    return elem_list, n_comparisons

print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([2, 1, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 2, 1]))

""" Sorts numbers in ascending order using insertion sort algorithm,
It modifies the original list.

Args: elem_list (list)

Returns: tuple[list,int] --> (insertion sort ordered list, number of comparisons) 
"""
def insertion_sort(elem_list):
    n_comparisons = 0
    for i in range(1,len(elem_list)):
        for k in range(i, 0, -1):
            n_comparisons+=1
            if elem_list[k] < elem_list[k-1]:
                elem_list[k], elem_list[k-1] = elem_list[k-1], elem_list[k]
            else: break
        
    return elem_list, n_comparisons

print(insertion_sort([1, 2, 3, 4, 5]))
print(insertion_sort([2, 1, 3, 4, 5]))
print(insertion_sort([5, 4, 3, 2, 1]))


""" Sorts numbers in ascending order using selection sort optimized algorithm.
It modifies the original list.

Args: elem_list (list)

Returns: tuple[list,int] --> (selection sort ordered list, number of comparisons) 
"""
def selection_sort(elem_list):
    n_comparisons = 0
    for i in range(0,len(elem_list)):
        pos_min_elem = i
        for k in range(i+1,len(elem_list)):
            n_comparisons += 1
            if elem_list[k] < elem_list[pos_min_elem]:
                pos_min_elem = k
        elem_list[i], elem_list[pos_min_elem] = elem_list[pos_min_elem], elem_list[i]
    
    return elem_list, n_comparisons

    
print(selection_sort([2,1,5,2,3,4]))

""" Finds an element from a list using a linear search algorithm.

Args:
    elem_list (list): List to search the item from
    item (item): Item  to search

Returns:
    tuple[int, int]: (index of the founded item (-1 if is not found), number of comparisons)
"""
def linear_search(elem_list, item):
    n_checks=0
    for i, el in enumerate(elem_list):
        n_checks+=1
        if el == item:
            return i, n_checks
    return -1, n_checks

print(linear_search([4,2,2,6,3,5,1,5,3,2,5,6,6,2,2,5,6,2], 1))

""" Search an element in a previous sorted list with a binary search algorithm.

Args:
    sorted_elem_list (list): List to search the item from
    item (item): Item  to search

Returns:
    tuple[int, int]: (index of the founded item (-1 if is not found), number of comparisons)
"""
def binary_search(sorted_elem_list, item):
    n_checks=0
    if not sorted_elem_list: return -1, n_checks
    left = 0
    right = len(sorted_elem_list)-1
    while True:
        middle = left + (right - left) // 2
        n_checks+=1
        if item == sorted_elem_list[middle]:
            return middle, n_checks
        if item > sorted_elem_list[middle]:
            left = middle + 1
        else: 
            right = middle - 1

        if right < left: return -1, n_checks
    

print(binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 16))

""" Calculate the factorial of a number

Args: num (int): Number to calculate factorial

Returns: (int): Factorial of the number
"""
def factorial_recursive(num):
    if num > 0: return num * factorial_recursive(num - 1)
    return 1

print(factorial_recursive(6))

""" Calculate the nth fibonacci number of the succession

Args: n_fib (int): Index of the fibbonacci succession number

Returns: (int): Fibonacci nth number
"""
def fibonacci_recursive(n_fib):
    if n_fib > 1: return fibonacci_recursive(n_fib - 1) + fibonacci_recursive(n_fib - 2)
    elif n_fib == 1: return 1
    else: return 0

print(fibonacci_recursive(3))

""" Search a value in a previous sorted list using recursive binary search

Args: 
    sorted_elem_list (list): List to search the item from
    item (item): Item  to search

Returns: 
    int: index of the founded item (-1 if is not found)
"""
def binary_search_recursive(sorted_elem_list, item, left=0, right=None):
    if not sorted_elem_list: return -1
    if right is None: right = len(sorted_elem_list) - 1
    if right < left: return -1
    middle = left + (right - left) // 2

    if item == sorted_elem_list[middle]:
        return middle
    if item > sorted_elem_list[middle]:
        return binary_search_recursive(sorted_elem_list, item, middle + 1, right)
    else:
        return binary_search_recursive(sorted_elem_list, item, left, middle - 1)

""" Merges to sorted lists in one sorted list in ascending order.
It does not modify the original lists.

Args:
    left_list (list): First sorted list.
    right_list (list): Second sorted list.

Returns:
    list: Unified sorted list.

"""
def merge(left_list, right_list):
    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left_list) and right_index < len(right_list):

        left_list_num = left_list[left_index]
        right_list_num = right_list[right_index]

        if right_list_num <= left_list_num:
            merged_list.append(right_list_num)
            right_index+=1
        else:
            merged_list.append(left_list_num)
            left_index+=1

    merged_list.extend(left_list[left_index:])
    merged_list.extend(right_list[right_index:])
    return merged_list

""" Sort a list in an ascendant order using the merge sort algorithm
It creates a copy of the original list.

Args: 
    elem_list (list): List to sort.

Returns:
    list: Sorted list.
"""
def merge_sort(elem_list):
    if len(elem_list) <= 1: return elem_list
    
    middle = len(elem_list) // 2
    left_list = merge_sort(elem_list[:middle])
    right_list = merge_sort(elem_list[middle:])

    return merge(left_list, right_list)

    
mylist = [2,5,6,1,3,4]
merge_sort(mylist)
print(mylist)

