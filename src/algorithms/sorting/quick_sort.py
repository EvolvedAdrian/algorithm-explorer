def quick_sort(elem_list):
    """ Sort a list in an ascendant order using the quick sort algorithm.
    It creates a copy of the original list.

    Time complexity:
        Best: O(n * logn)
        Average: O(n * logn)
        Worst: O(n2)

    Space complexity: O(n)

    Args:
        elem_list (list): List to sort.

    Returns:
        list: Sorted list.
    """
    if len(elem_list) <= 1:
        return elem_list

    pivot = elem_list[-1]
    left_list = []
    right_list = []

    # Partition elements around the pivot.
    for i, el in enumerate(elem_list):
        # Avoid the pivot to be appended to the left or right list.
        if i == len(elem_list) - 1:
            continue
        if el < pivot:
            left_list.append(el)
        else:
            right_list.append(el)

    left_list = quick_sort(left_list)
    right_list = quick_sort(right_list)

    sorted_list = []
    sorted_list.extend(left_list)
    sorted_list.append(pivot)
    sorted_list.extend(right_list)

    return sorted_list
