""" Finds an element from a list using a linear search algorithm.

Time complexity:
    Best: O(1)
    Average: O(n)
    Worst: O(n)

Space complexity: O(1)

Args:
    elem_list (list): List to search the item from.
    item (item): Item  to search.

Returns:
    int: Index of the founded item (-1 if is not found).
"""
def linear_search(elem_list, item):
    for i, el in enumerate(elem_list):
        if el == item:
            return i

    return -1
