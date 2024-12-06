#State of the program right berfore the function call: arr is a list of elements of any type.
def func_1(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_index = find_max_index(curr_size)
        
        if max_index != curr_size - 1:
            flip(max_index)
            flip(curr_size - 1)
        
    #State of the program after the  for loop has been executed: `arr` is a list with elements sorted in non-increasing order, `n` is the length of the original list, and `curr_size` will be 1 after the loop completes. The value of `max_index` will correspond to the index of the maximum remaining element in the subarray considered until the last iteration. If `n` was less than or equal to 1, the loop does not execute and `arr` remains unchanged.
    return arr
    #The program returns the list 'arr' which is sorted in non-increasing order and unchanged if 'n' is less than or equal to 1
#Overall this is what the function does:The function accepts a list `arr` containing elements of any type and returns the list sorted in non-increasing order. If the length of `arr` is 1 or less, the function returns the list unchanged.

#State of the program right berfore the function call: end is a non-negative integer representing the last index of the list to be reversed, and start is implicitly defined as starting from 0.
def flip(end):
    start = 0
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        
        start += 1
        
        end -= 1
        
    #State of the program after the loop has been executed: `start` is equal to `end + 1`, `end` is now less than the original value of `end`, and the elements of `arr` have been reversed from the original arrangement between the indices 0 and the original value of `end`. If the original value of `end` was odd, the middle element remains unchanged; if it was even, all elements are swapped.
#Overall this is what the function does:The function accepts a non-negative integer `end`, and it reverses the elements of a global list `arr` from index `0` to `end`. The function does not explicitly handle cases where `arr` is not defined or when `end` is greater than the length of `arr`, which could lead to an IndexError. If `end` is less than `0`, the function will not perform any operation.

#State of the program right berfore the function call: n is a positive integer representing the length of the list, and arr is a list of elements with at least n elements.
def find_max_index(n):
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `arr` is a list of elements with at least `n` elements, `max_index` is the index of the maximum element in `arr` from the first `n` elements.
    return max_index
    #The program returns the index of the maximum element in the list 'arr' from the first 'n' elements.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the index of the maximum element in a global list `arr` from the first `n` elements. If `n` is greater than the length of `arr`, this could potentially lead to an IndexError, as the function does not handle cases where `n` exceeds the number of available elements in `arr`.

