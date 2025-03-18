#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr).
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: `i` is the index of the first element in `arr` that is not equal to its next element, or `len(arr) - 1` if all elements are equal. `j` remains `n - 1`.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: `i` remains the same, `j` is the index of the last element in `arr` that is not equal to its previous element, or `0` if all elements are equal.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum value between 0 and (j - i - 1), where `j` is the index of the last element in `arr` that is not equal to its previous element, or 0 if all elements are equal, and `i` remains the same.
    #State: *`i` remains the same, `j` is the index of the last element in `arr` that is not equal to its previous element, or `0` if all elements are equal. The first element of `arr` is not equal to the last element of `arr`.
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum of 0 and the minimum of (n - i - 1) and `j`, where `j` is the index of the last element in `arr` that is not equal to its previous element, or `0` if all elements are equal, and `n` is the length of `arr`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and returns a value based on the indices of elements that are not equal to their adjacent elements. If all elements in `arr` are equal, it returns 0. Otherwise, it returns the length of the longest contiguous subarray of equal elements that is not at the beginning or end of `arr`, or 0 if no such subarray exists.

