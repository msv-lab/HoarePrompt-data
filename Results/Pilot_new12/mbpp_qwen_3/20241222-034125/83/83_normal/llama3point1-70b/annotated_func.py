#State of the program right berfore the function call: arr is a list of elements (can be integers, floats, strings, etc.).
def func_1(arr):
    n = len(arr)
    for size in range(n, 0, -1):
        max_index = arr.index(max(arr[:size]))
        
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
        
    #State of the program after the  for loop has been executed: `arr` is a sorted list in non-decreasing order, `n` is the length of `arr`, and `size` is 1.
    return arr
    #`The program returns the sorted list 'arr' which has a length of n`
#Overall this is what the function does:The function `func_1` accepts a list `arr` as a parameter and returns the same list sorted in non-decreasing order. It achieves this by iterating over the list in reverse order of sizes, finding the maximum element within each size range, and reversing the appropriate segments of the list to ensure the maximum element moves towards the beginning of the current segment. If the maximum element is not already in the correct position, it reverses the segment up to the maximum index. This process continues until the entire list is sorted. Potential edge cases include lists with duplicate elements, empty lists, or lists with a single element, all of which are handled correctly by the function.

