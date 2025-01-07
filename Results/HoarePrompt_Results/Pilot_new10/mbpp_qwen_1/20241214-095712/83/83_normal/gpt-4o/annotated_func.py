#State of the program right berfore the function call: arr is a list of elements (can be of any comparable type).
def func_1(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_index = find_max_index(curr_size)
        
        if max_index != curr_size - 1:
            flip(max_index)
            flip(curr_size - 1)
        
    #State of the program after the  for loop has been executed: `arr` is sorted in non-decreasing order, `curr_size` is 1, `max_index` is not defined (or can be any value since it's out of scope), `n` is the original length of `arr` and is now less than 2.
    return arr
    #`The program returns the sorted list 'arr' with its current size being 1`
#Overall this is what the function does:The function accepts a list `arr` and sorts it in non-decreasing order using a specific swapping mechanism. If the array has fewer than 2 elements, it returns the array as is. After processing, the array is sorted, and its size is reduced to 1.

#State of the program right berfore the function call: `arr` is a list of elements, and `end` is an integer such that 0 <= end < len(arr).
def flip(end):
    start = 0
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        
        start += 1
        
        end -= 1
        
    #State of the program after the loop has been executed: `arr` is a list of elements where the elements at indices `start` and `end` are swapped, `start` is equal to `end + 1`, `end` is equal to `-1`, and `start` must have been less than `end` initially.
#Overall this is what the function does:The function accepts an integer `end` and reverses the sublist of `arr` from index 0 to `end` (inclusive). This is achieved by swapping elements at indices `start` and `end`, incrementing `start` and decrementing `end` until `start` becomes greater than or equal to `end`.

#State of the program right berfore the function call: arr is a list of comparable elements, and n is an integer such that 0 < n <= len(arr).
def find_max_index(n):
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
        
    #State of the program after the  for loop has been executed: `arr` is a list of comparable elements, `n` is an integer such that 0 < n ≤ len(arr), and `max_index` is the index of the maximum element in the subarray `arr[0:n]`.
    return max_index
    #The program returns the index of the maximum element in the subarray `arr[0:n]`
#Overall this is what the function does:The function accepts a list `arr` and an integer `n`, and returns the index of the maximum element in the subarray `arr[0:n]`. This is achieved by iterating through the subarray from index 1 to `n-1` and updating the index of the maximum element whenever a larger element is found.

