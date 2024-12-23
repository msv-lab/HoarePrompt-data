#State of the program right berfore the function call: arr is a list of elements (can be of any comparable type).
def func_1(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_index = find_max_index(curr_size)
        
        if max_index != curr_size - 1:
            flip(max_index)
            flip(curr_size - 1)
        
    #State of the program after the  for loop has been executed: `arr` is a list of elements where the largest element is at the last position, `n` is the length of the original array, and `curr_size` is 2.
    return arr
    #The program returns the list 'arr' where the largest element is at the last position
#Overall this is what the function does:The function `func_1` accepts a list `arr` as a parameter and ensures that the largest element in the list is moved to the last position. It achieves this by iterating over the list from the second-largest element to the first, finding the index of the current maximum element, and swapping it with the current element if necessary. After the loop completes, the function returns the modified list `arr`. Potential edge cases include an empty list or a list with only one element, in which case the function would return the list unchanged. The function also assumes that the list contains elements that can be compared.

#State of the program right berfore the function call: arr is a list of elements, and end is an integer such that 0 <= end < len(arr), representing the last index of the sublist to be sorted.
def flip(end):
    start = 0
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        
        start += 1
        
        end -= 1
        
    #State of the program after the loop has been executed: `start` is equal to `end` + 1, `end` is equal to the original value of `end` which satisfies \(0 \leq \text{end} < \text{len(arr)}\), and `arr` is reversed.
#Overall this is what the function does:The function `flip` takes an integer `end` as a parameter, where `0 <= end < len(arr)` and `arr` is a list of elements. It reverses the sublist of `arr` from index `0` to `end` (inclusive). After the function executes, `arr` will have its elements in reverse order from index `0` to `end`, while the rest of the list remains unchanged. If `end` is 0 or negative, the function will do nothing because the loop condition `start < end` will never be met. The function does not return any value.

#State of the program right berfore the function call: arr is a list of comparable elements (e.g., integers, floats, strings), and n is an integer representing the length of the list such that 1 <= n <= len(arr).
def find_max_index(n):
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
        
    #State of the program after the  for loop has been executed: `arr` is a list of comparable elements, `n` is a positive integer such that 1 <= n <= len(arr), `max_index` is the index of the maximum element in `arr` (if such an element exists), otherwise `max_index` remains 0.
    return max_index
    #`The program returns max_index which is the index of the maximum element in `arr` if such an element exists, otherwise it remains 0
#Overall this is what the function does:The function `find_max_index` accepts an integer `n` representing the length of a list `arr` and returns the index of the maximum element in `arr` if such an element exists. If no maximum element is found, it returns 0. The function iterates through the list `arr` starting from index 1 up to `n-1` to find the maximum element. If the list is empty (i.e., `n` is less than 1), the function would not enter the loop and `max_index` would remain 0, satisfying the postcondition. However, since the precondition ensures `1 <= n <= len(arr)`, this edge case is covered within the given constraints.

