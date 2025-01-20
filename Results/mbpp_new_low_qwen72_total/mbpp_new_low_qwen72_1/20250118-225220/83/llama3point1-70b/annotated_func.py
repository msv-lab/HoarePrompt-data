#State of the program right berfore the function call: arr is a list of comparable elements.
def func_1(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_index = arr.index(max(arr[:size]))
        
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
        
    #State of the program after the  for loop has been executed: `arr` is sorted in non-decreasing order, `n` is the length of `arr`, and `size` is `0` (though `size` is not relevant in the final state).
    return arr
    #The program returns `arr`, which is a list sorted in non-decreasing order.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of comparable elements and returns the list sorted in non-decreasing order. The function uses a variant of the selection sort algorithm, where it repeatedly finds the maximum element in the unsorted portion of the list and moves it to the end of the unsorted portion. If the maximum element is not already in its correct position, the function performs swaps by reversing sublists. After the function completes, `arr` is guaranteed to be sorted in non-decreasing order, and the original list is modified in place. Edge cases include handling empty lists or lists with a single element, both of which will be returned as-is since they are already considered sorted.

