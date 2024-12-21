#State of the program right berfore the function call: arr is a list of comparable elements (e.g., integers, strings, etc.).
def func_1(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_index = find_max_index(curr_size)
        
        if max_index != curr_size - 1:
            flip(max_index)
            flip(curr_size - 1)
        
    #State of the program after the  for loop has been executed: `arr` is a list of comparable elements; `n` is the length of `arr`; the list `arr` is sorted in descending order.
    return arr
    #`arr` which is a list of comparable elements sorted in descending order
#Overall this is what the function does:The function `func_1` accepts a list `arr` of comparable elements and returns the same list sorted in descending order. It achieves this by iterating over the list from the end to the beginning, finding the index of the maximum element in the current subarray, and swapping it with the last element of the subarray. This process is repeated until the entire list is sorted in descending order. The function handles the case where the maximum element is already in its correct position, avoiding unnecessary swaps. However, it does not handle the case where the input list is already sorted in descending order, as no changes would be made in such a scenario.

#State of the program right berfore the function call: arr is a list of elements, and end is an integer such that 0 <= end < len(arr), indicating the end index of the sublist to be flipped.
def flip(end):
    start = 0
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        
        start += 1
        
        end -= 1
        
    #State of the program after the loop has been executed: `start` is equal to `end + 1`, `end` is 0, and every pair of elements that were originally at indices `(i, len(arr) - 1 - i)` where `i` ranges from `0` to `start - 1` have been swapped.
#Overall this is what the function does:The function `flip` takes an integer `end` as a parameter, where `0 <= end < len(arr)`, and reverses the sublist of the list `arr` from index `0` to `end` inclusive. After executing the function, the elements in `arr` from index `0` to `end` will be in reverse order, with the element originally at index `0` now at index `end`, and the element originally at index `end` now at index `0`. If `end` is `0`, the function does nothing since there are no elements to flip. The function also ensures that after the flip operation, the value of `start` becomes equal to `end + 1`, and `end` becomes `0`, indicating that the entire sublist has been processed.

#State of the program right berfore the function call: arr is a list of comparable elements, and n is an integer representing the length of the list such that 0 < n <= len(arr).
def find_max_index(n):
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` must be greater than 1, `arr` must have at least `n` elements, and `max_index` is the index of the maximum element in `arr` if the loop executes at least once. Otherwise, `max_index` remains 0.
    return max_index
    #`The program returns max_index, which is the index of the maximum element in list 'arr' if the loop executes at least once. Otherwise, max_index remains 0.`
#Overall this is what the function does:The function `find_max_index` accepts an integer `n` representing the length of the list `arr`. It iterates through the first `n` elements of `arr` to find the index of the maximum element. If the loop executes at least once, it returns the index of the maximum element. If the loop does not execute (i.e., the list is empty or `n` is 1), it returns 0. An edge case to consider is when `n` is 0, in which case the function should return 0 immediately without entering the loop. Additionally, the function assumes that `arr` has at least `n` elements, which might not always be true; thus, the function should handle this case by checking the length of `arr` against `n` before proceeding with the loop.

