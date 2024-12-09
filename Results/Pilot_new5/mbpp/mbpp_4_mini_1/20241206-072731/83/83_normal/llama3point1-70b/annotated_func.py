#State of the program right berfore the function call: arr is a list of elements that can be compared to each other.
def func_1(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_index = arr.index(max(arr[:size]))
        
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
        
    #State of the program after the  for loop has been executed: `arr` is sorted in non-decreasing order, `n` is a non-negative integer, and if `n` is greater than 0, the loop has executed `n` times. If `n` is 0, `arr` remains unchanged and empty.
    return arr
    #The program returns the sorted array 'arr' which is in non-decreasing order and is either unchanged and empty if n is 0, or has been modified through 'n' executions of a loop if n is greater than 0.
#Overall this is what the function does:The function accepts a list `arr` and sorts the elements in non-decreasing order using a selection sort-like algorithm. If `arr` is empty, it returns an unchanged empty list. If `arr` contains elements, it modifies `arr` in-place and returns the sorted list.

