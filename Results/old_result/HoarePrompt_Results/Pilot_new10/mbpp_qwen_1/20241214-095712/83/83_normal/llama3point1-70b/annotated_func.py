#State of the program right berfore the function call: arr is a list of elements (can be of any type that supports comparison).
def func_1(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_index = arr.index(max(arr[:size]))
        
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list in descending order, `n` is the original length of `arr`, `max_index` is the index of the maximum element in the final sorted list.
    return arr
    #The program returns the sorted list `arr` in its original descending order
#Overall this is what the function does:The function `func_1` accepts a list `arr` and returns the list sorted in descending order. For each possible size from the length of `arr` down to 1, it finds the index of the maximum element in the current subarray. If the maximum element is not at the end of the current subarray, it reverses the prefix up to the maximum element's index and then reverses the entire current subarray. This ensures that the maximum element is moved to the end of the current subarray. After the loop completes, the function returns the fully sorted list in descending order.

