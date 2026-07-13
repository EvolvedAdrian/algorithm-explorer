""" Search a value in a previous sorted list using recursive binary search.

Args: 
    sorted_elem_list (list): List to search the item from.
    item (item): Item  to search.

Returns: 
    int: Index of the founded item (-1 if is not found).
"""
def binary_search_recursive(sorted_elem_list, item, left=0, right=None):
    if not sorted_elem_list: 
        return -1
    if right is None: 
        right = len(sorted_elem_list) - 1
    if right < left: 
        return -1
    middle = left + (right - left) // 2

    # Adapt the searching window recursively to the left and right to look for the element.
    if item == sorted_elem_list[middle]:
        return middle
    if item > sorted_elem_list[middle]:
        return binary_search_recursive(sorted_elem_list, item, middle + 1, right)
    else:
        return binary_search_recursive(sorted_elem_list, item, left, middle - 1)