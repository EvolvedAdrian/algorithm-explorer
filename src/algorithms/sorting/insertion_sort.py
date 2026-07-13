""" Sorts numbers in ascending order using insertion sort algorithm.
It modifies the original list.

Args:
    elem_list (list): List to sort.

Returns:
    list: Sorted list.
"""
def insertion_sort(elem_list):
    for i in range(1,len(elem_list)):
        for k in range(i, 0, -1):
            # Translate the smallest element to its correct position.
            if elem_list[k] < elem_list[k-1]:
                elem_list[k], elem_list[k-1] = elem_list[k-1], elem_list[k]
            else:
                # When the current element is in its final position no more comparisons are needed.
                break

    return elem_list
