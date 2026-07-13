""" Sorts numbers in ascending order using insertion sort algorithm.
It modifies the original list.

Args: 
    elem_list (list): List to sort.

Returns: 
    tuple[list,int]: Sorted list, number of comparisons.
"""
def insertion_sort(elem_list):
    n_comparisons = 0

    for i in range(1,len(elem_list)):
        for k in range(i, 0, -1):
            n_comparisons+=1
            
            # Translate the smallest element to its correct position.
            if elem_list[k] < elem_list[k-1]:
                elem_list[k], elem_list[k-1] = elem_list[k-1], elem_list[k]
            else:
                # When the current element is in its final position no more comparisons are needed.
                break
        
    return elem_list, n_comparisons