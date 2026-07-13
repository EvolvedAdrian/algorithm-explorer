""" Sorts numbers in ascending order using selection sort optimized algorithm.
It modifies the original list.

Args: 
    elem_list (list): List to sort.

Returns: 
    tuple[list,int]: Sorted list, number of comparisons.
"""
def selection_sort(elem_list):
    n_comparisons = 0

    for i in range(0,len(elem_list)):
        min_index = i

        # Find min_index for the next list items. 
        for k in range(i+1,len(elem_list)):
            n_comparisons += 1

            if elem_list[k] < elem_list[min_index]:
                min_index = k

        # Place the smallest element in its final position.
        elem_list[i], elem_list[min_index] = elem_list[min_index], elem_list[i]
    
    return elem_list, n_comparisons