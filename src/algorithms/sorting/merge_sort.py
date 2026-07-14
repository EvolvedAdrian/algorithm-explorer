def merge(left_list, right_list):
    """ Merges two sorted lists in one sorted list in ascending order.
    It does not modify the original lists.

    Time complexity:
        Best: O(n)
        Average: O(n)
        Worst: O(n)

    Space complexity: O(n)

    Args:
        left_list (list): First sorted list.
        right_list (list): Second sorted list.

    Returns:
        list: Unified sorted list.
    """
    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left_list) and right_index < len(right_list):

        left_list_num = left_list[left_index]
        right_list_num = right_list[right_index]

        # Append the smallest element to the merged list.
        if right_list_num <= left_list_num:
            merged_list.append(right_list_num)
            right_index+=1
        else:
            merged_list.append(left_list_num)
            left_index+=1

    # Ensure to include rest of the numbers in the final list.
    merged_list.extend(left_list[left_index:])
    merged_list.extend(right_list[right_index:])
    return merged_list

def merge_sort(elem_list):
    """ Sort a list in ascending order using the merge sort algorithm.
    It creates a copy of the original list.

    Time complexity:
        Best: O(n * logn)
        Average: O(n * logn)
        Worst: O(n * logn)

    Space complexity: O(n)

    Args:
        elem_list (list): List to sort.

    Returns:
        list: Sorted list.
    """
    if len(elem_list) <= 1:
        return elem_list
    middle = len(elem_list) // 2
    
    # Divide the list recursively in left and right.
    left_list = merge_sort(elem_list[:middle])
    right_list = merge_sort(elem_list[middle:])

    return merge(left_list, right_list)