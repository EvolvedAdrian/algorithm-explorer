""" Sorts numbers in ascending order using bubble sort optimized algorithm.
It modifies the original list.

Args:
    elem_list (list): List to sort.

Returns:
    list: Sorted list.
"""
def bubble_sort(elem_list):
    # Optimizations
    array_sorted = False
    ordered_numbers = 0

    while not array_sorted:
        array_sorted = True

        # Each pass translates the biggest number to its final position (in the end).
        # Skip the last "ordered_numbers" because they are already in their final position.
        for i in range(1, len(elem_list)-ordered_numbers):
            if elem_list[i] < elem_list[i-1]:
                array_sorted = False
                elem_list[i], elem_list[i-1] = elem_list[i-1], elem_list[i]

        ordered_numbers+=1

    return elem_list
