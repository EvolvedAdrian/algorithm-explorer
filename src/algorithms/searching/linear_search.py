""" Finds an element from a list using a linear search algorithm.

Args:
    elem_list (list): List to search the item from.
    item (item): Item  to search.

Returns:
    tuple[int, int]: (index of the founded item (-1 if is not found), number of comparisons.
"""
def linear_search(elem_list, item):
    n_checks=0

    for i, el in enumerate(elem_list):
        n_checks+=1

        if el == item:
            return i, n_checks
        
    return -1, n_checks