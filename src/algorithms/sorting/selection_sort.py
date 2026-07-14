""" Sorts numbers in ascending order using selection sort optimized algorithm.
It modifies the original list.

Time complexity:
    Best: O(n2)
    Average: O(n2)
    Worst: O(n2)

Space complexity: O(1)

Args:
    elem_list (list): List to sort.

Returns:
    list: Sorted list.
"""
def selection_sort(elem_list):
    for i in range(0,len(elem_list)):
        min_num_index = i

        # Find min_num_index for the next list items.
        for k in range(i+1,len(elem_list)):
            if elem_list[k] < elem_list[min_num_index]:
                min_num_index = k

        # Place the smallest element in its final position.
        elem_list[i], elem_list[min_num_index] = elem_list[min_num_index], elem_list[i]

    return elem_list
