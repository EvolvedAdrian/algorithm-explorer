""" Search an element in a previous sorted list with a binary search algorithm.

Args:
    sorted_elem_list (list): List to search the item from.
    item (item): Item  to search.

Returns:
    int: Index of the founded item (-1 if is not found).
"""
def binary_search(sorted_elem_list, item):
    if not sorted_elem_list:
        return -1
    left = 0
    right = len(sorted_elem_list)-1

    while True:
        middle = left + (right - left) // 2

        # We keep adapting the searching window with left and right until middle == item to search
        if item == sorted_elem_list[middle]:
            return middle
        if item > sorted_elem_list[middle]:
            left = middle + 1
        else:
            right = middle - 1

        if right < left:
            return -1
