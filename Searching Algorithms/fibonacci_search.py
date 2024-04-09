
'''
    Fibonacci search can be used in situations where the array size 
    is large and the division operation is costly. It reduces the number 
    of comparisons needed to find the target element compared to binary search. 
    Fibonacci search is particularly useful when the array size is not known in 
    advance or when the array size changes dynamically.
'''

# Time Complexity: O(log n) -> n is the size of the array.
# Space Complexity: O(1)

def fibonacci_search(arr, target):
    size = len(arr)

    # Initialize Fibonacci numbers
    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1

    # Find the smallest Fibonacci number greater than or equal to the array size
    while fib < size:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
    
    offset = -1

    while fib > 1:
        i = min(offset + fib2, size - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        
        else:
            return i
        
    if fib1 and arr[offset + 1] == target:
        return offset + 1
    
    return -1