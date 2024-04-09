
'''
    Binary search is an efficient algorithm for finding an element
    in a sorted list by repeatedly dividing the search space in half 
    until the target element is found or the search space is exhausted.
'''

# Time Complexity: O(log n) -> n is the size of the input list.
# Space Complexity: O(1) -> constant amount of extra space is used.

def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


# Time Complexity: O(log n) - n is the size fo the input list.
# Space Complexity: O(lon n) - n is the size of the input list. 
# This is because at every run "another half" of the array is stored in the stack. DONT ever implement this. It is stupid.

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
