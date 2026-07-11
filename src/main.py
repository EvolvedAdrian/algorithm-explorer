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