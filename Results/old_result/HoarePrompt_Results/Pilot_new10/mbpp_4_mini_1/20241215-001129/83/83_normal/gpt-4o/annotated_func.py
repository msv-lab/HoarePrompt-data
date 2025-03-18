#State of the program right berfore the function call: arr is a list of elements of any type.
def func_1(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_index = find_max_index(curr_size)
        
        if max_index != curr_size - 1:
            flip(max_index)
            flip(curr_size - 1)
        
    #State of the program after the  for loop has been executed: `arr` is a list of elements of any type sorted in decreasing order, `n` is 1 (as the loop will stop when curr_size becomes less than or equal to 1), and `curr_size` has been decremented from the original length of `arr` down to 1.
    return arr
    #The program returns the list 'arr' which is sorted in decreasing order.
#Overall this is what the function does:The function accepts a list `arr` of elements of any type and sorts it in decreasing order using a sorting algorithm that involves flipping elements based on their indices. The function returns the sorted list.

#State of the program right berfore the function call: end is a non-negative integer such that end < len(arr), and start is initialized to 0.
def flip(end):
    start = 0
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        
        start += 1
        
        end -= 1
        
    #State of the program after the loop has been executed: `start` is equal to `end`, `end` is reduced to an initial value minus the number of times the loop executed, and the array `arr` has had its elements reversed between indices 0 and the original value of `end`. If `end` was originally greater than `start`, the loop executed fully, swapping elements until the middle of the array was reached. If `end` was not greater than `start`, the loop did not execute, and the array remains unchanged.
#Overall this is what the function does:The function accepts a non-negative integer `end` (less than the length of the global list `arr`) and reverses the elements of `arr` from index 0 to index `end`. If `end` is 0, the function does not modify the array as there are no elements to swap. The function does not return anything, as it directly modifies the list `arr` in place.

#State of the program right berfore the function call: n is a positive integer representing the length of the list arr, which must be defined in the scope of the function.
def find_max_index(n):
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
        
    #State of the program after the  for loop has been executed: 
    return max_index
    #The program returns the value of 'max_index', which represents the index of the maximum element in a given list or dataset.
#Overall this is what the function does:The function accepts a positive integer `n`, and returns the index of the maximum element in the list `arr`. It does not handle cases where `arr` is empty or when `n` is 0, potentially leading to incorrect results. If all elements are equal, it will return 0.

