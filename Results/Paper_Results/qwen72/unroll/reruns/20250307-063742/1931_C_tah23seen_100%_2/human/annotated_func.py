#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr).
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: `i` is the index of the first element in `arr` that is not equal to its next element, or `i` is `len(arr) - 1` if all elements are equal. `j` remains `n - 1`.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: `i` remains the same, and `j` is the index of the first element in `arr` that is not equal to its next element, or `0` if all elements are equal.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum of 0 and (j - i - 1), where `j` is the index of the first element in `arr` that is not equal to its next element, or 0 if all elements are equal, and `i` remains the same.
    #State: *`i` remains the same, and `j` is the index of the first element in `arr` that is not equal to its next element, or `0` if all elements are equal. Additionally, the first element of `arr` is not equal to the last element of `arr`.
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum value between 0 and the minimum of (n - i - 1) and j, where n is the length of the list `arr`, `i` remains the same, and `j` is the index of the first element in `arr` that is not equal to its next element, or 0 if all elements are equal.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and returns the length of the longest subarray of consecutive equal elements, excluding the first and last elements if they are the same. If all elements in the list are equal, it returns 0. If the first and last elements are different, it returns the length of the subarray from the first non-equal element to the last non-equal element, or 0 if no such subarray exists.

