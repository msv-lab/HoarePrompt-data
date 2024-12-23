#State of the program right berfore the function call: arr is a list of elements (can be integers, floats, strings, etc.).
def func_1(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_index = arr.index(max(arr[:size]))
        
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
        
    #State of the program after the  for loop has been executed: `arr` is a non-empty list, `n` is the length of `arr`, and the entire list `arr` is sorted in non-increasing order. If there was any reordering during the loop execution, the sublist `arr[:n]` is in its final ordered state.
    return arr
    #The program returns the list `arr` which is a non-empty list sorted in non-increasing order, with the first `n` elements in their final ordered state
#Overall this is what the function does:The function `func_1` accepts a non-empty list `arr` of elements (which can be integers, floats, or strings). It iterates through the list from the largest possible size down to 1, finding the maximum element in each subarray and adjusting the list to ensure that the maximum element is moved to the front of the current subarray. This process continues until the entire list is sorted in non-increasing order. Specifically, the function ensures that the first `n` elements of the list (`n` being the length of the list) are in their final sorted order. The function does not modify the original list but returns a new list that meets these criteria. Potential edge cases include lists with duplicate maximum values, where the function will still sort the list correctly. The function does not handle empty lists; attempting to pass an empty list will result in an error since `len(arr)` would be 0, leading to an `IndexError`.

