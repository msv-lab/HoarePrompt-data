#State of the program right berfore the function call: arr is a list of elements, and find_max_index and flip are functions that operate on arr, with find_max_index taking an integer argument and returning an index, and flip taking an integer argument and modifying arr in place.
def func_1(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_index = find_max_index(curr_size)
        
        if max_index != curr_size - 1:
            flip(max_index)
            flip(curr_size - 1)
        
    #State of the program after the  for loop has been executed: `arr` is sorted in descending order, `n` is the length of the sorted `arr`, `curr_size` is 2.
    return arr
    #The program returns array `arr` which is sorted in descending order and has a length of `n`.
#Overall this is what the function does:The function accepts a list of elements `arr` as input and returns the same list sorted in descending order, with its length unchanged. The function operates on the input list in-place, modifying it directly, and does not create a new sorted list. The sorting process is achieved through a series of flips or swaps, utilizing the `find_max_index` and `flip` functions, which are not defined within this code snippet but are assumed to be available. After the function executes, the input list `arr` will be sorted in descending order, and its length will remain the same as the original input. The function does not handle cases where the input list is empty or contains non-comparable elements, and it assumes that the `find_max_index` and `flip` functions are correctly implemented to work with the list.

#State of the program right berfore the function call: arr is a list of elements, and end is a non-negative integer such that 0 <= end < len(arr).
def flip(end):
    start = 0
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        
        start += 1
        
        end -= 1
        
    #State of the program after the loop has been executed: `arr` has its elements reversed between the original `start` (0) and `end` indices, `start` equals the original value of `end`, and `end` equals 0
#Overall this is what the function does:The function `flip` reverses the order of elements in the list `arr` from the start (index 0) to the specified `end` index. It modifies the original list in-place and does not return any value. After execution, the elements in `arr` between indices 0 and the original value of `end` are reversed, while the rest of the list remains unchanged. The function handles cases where `end` is 0 or greater, up to but not including the length of `arr`, and does not explicitly handle cases where `end` is greater than or equal to the length of `arr` or less than 0, as these are assumed to be invalid inputs based on the provided annotations. If `arr` has one or zero elements, or if `end` is 0, the function does not alter the list, effectively acting as an identity function for these edge cases. The function's effect is solely on the input list `arr`, and it does not produce a new list or value as output.

#State of the program right berfore the function call: arr is a list of elements, and n is a non-negative integer such that 0 <= n <= len(arr)
def find_max_index(n):
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
        
    #State of the program after the  for loop has been executed: `arr` is a list of elements, `n` is a non-negative integer such that `n` <= `len(arr)`, `max_index` is the index of the maximum element in `arr[0:n]`, and `i` is `n-1` if `n` > 1, otherwise `i` is unspecified as the loop doesn't execute.
    return max_index
    #The program returns the index of the maximum element in the sublist `arr[0:n]`, where `n` is a non-negative integer and `arr` is a list of elements
#Overall this is what the function does:The function accepts two parameters: a non-negative integer `n` and a list `arr`. It returns the index of the maximum element in the sublist `arr[0:n]`. If `n` is 0, the function will return 0, as there are no elements in the sublist. If `n` is 1, the function will return 0, as there is only one element in the sublist. For `n` greater than 1, the function will iterate through the sublist and return the index of the maximum element. If all elements in the sublist are equal, the function will return 0, as it is the index of the first occurrence of the maximum element. The function does not modify the input list `arr` and does not handle cases where `n` is greater than the length of `arr`, although the annotations suggest that `n` is a non-negative integer such that `0 <= n <= len(arr)`. However, the actual code does not check for this condition, and it is assumed that `arr` is defined and accessible within the function's scope, although it is not passed as a parameter to the function.

