#State of the program right berfore the function call: arr is a list of elements (can be of any type that supports comparison).
def func_1(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_index = find_max_index(curr_size)
        
        if max_index != curr_size - 1:
            flip(max_index)
            flip(curr_size - 1)
        
    #State of the program after the  for loop has been executed: `arr` is a list of elements where the first `n-1` elements are in their original order; the element at `max_index` is swapped with the last element; `curr_size` is 1; `max_index` is the index of the maximum element in the first `1` element of `arr` (which is just the last element).
    return arr
    #`arr' where the last element is swapped with the maximum element in the first '1' element of 'arr', 'curr_size' is 1, and 'max_index' is the index of the maximum element in the first '1' element of 'arr'
#Overall this is what the function does:The function `func_1` accepts a list `arr` and returns a modified list `arr'`. After executing the function, the last element of the list is swapped with the maximum element among the first `n-1` elements of the list, where `n` is the length of the list. The variable `curr_size` is set to 1, indicating that only one element is being considered in the final step. The variable `max_index` is the index of the maximum element among the first `n-1` elements of the list. If the maximum element is already in its correct position (i.e., the last position), no swap occurs. This process effectively ensures that the last element of the list is the maximum among the first `n-1` elements. The function handles edge cases where the list might be empty or contain a single element, in which case no action is performed.

#State of the program right berfore the function call: arr is a list of elements (can be of any type), and end is an integer such that 0 <= end < len(arr).
def flip(end):
    start = 0
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        
        start += 1
        
        end -= 1
        
    #State of the program after the loop has been executed: `arr` is reversed, `start` is equal to `end + 1`, `end` is equal to its original value
#Overall this is what the function does:The function `flip(end)` takes a list `arr` and an integer `end` as input and reverses the elements in `arr` from the beginning up to the index `end`. After the function execution, the elements in `arr` from index 0 to `end` will be reversed, `start` will be equal to `end + 1`, and `end` will retain its original value. If `end` is less than half the length of `arr`, only the first `end + 1` elements will be reversed. If `end` is exactly half the length of `arr`, the first `end + 1` elements will be reversed, and the rest of the list will remain unchanged.

#State of the program right berfore the function call: arr is a list of comparable elements (e.g., integers, floats, strings), and n is an integer representing the length of the list such that 1 <= n <= len(arr).
def find_max_index(n):
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
        
    #State of the program after the  for loop has been executed: `arr` is a list of comparable elements, `n` is a positive integer, `max_index` is the index of the maximum element in the list `arr`, and `i` is `n`.
    return max_index
    #`The program returns the index of the maximum element in the list 'arr'`
#Overall this is what the function does:The function `find_max_index` accepts an integer `n` representing the length of the list `arr`. It iterates through the list `arr` from index 1 to `n-1` to find the index of the maximum element. If the list `arr` is empty or `n` is less than 1, the function will raise an `IndexError` because the loop will not execute. After finding the index of the maximum element, the function returns this index. The function ensures that the returned index is valid within the bounds of the list `arr`.

