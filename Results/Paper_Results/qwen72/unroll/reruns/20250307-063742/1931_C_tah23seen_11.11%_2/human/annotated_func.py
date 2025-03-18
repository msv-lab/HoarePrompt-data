#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr).
def func_1(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        else:
            break
        
    #State: `i` is greater than `j` or `arr[i]` is not equal to `arr[j]`.
    if (i > j) :
        return 0
        #The program returns 0.
    #State: `i` is greater than or equal to `j` or `arr[i]` is not equal to `arr[j]`. `i` is not greater than `j`.
    while arr[i] == arr[i + 1]:
        i += 1
        
    #State: `i` is incremented to the point where `arr[i]` is not equal to `arr[i + 1]`, or `i` is equal to `j`.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns the difference between `j` and `i` plus 1, where `i` is the index at which `arr[i]` is not equal to `arr[i + 1]` or `i` is equal to `j`, and `j` is an index that is not the last index of `arr`.
    #State: *`i` is incremented to the point where `arr[i]` is not equal to `arr[i + 1]`, or `i` is equal to `j`. Additionally, `j` is equal to `len(arr) - 1`.
    return j - i
    #The program returns the difference between `j` and `i`, where `j` is equal to `len(arr) - 1` and `i` is the index where `arr[i]` is not equal to `arr[i + 1]`, or `i` is equal to `j`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and returns the length of the longest contiguous subarray where all elements are the same, starting from the first mismatched element or 0 if the array is a palindrome. Specifically, it returns 0 if the array is a palindrome (i.e., all elements are symmetrically equal), the difference between `j` and `i` plus 1 if `j` is not the last index of `arr` and the elements from `i` to `j` are the same, or the difference between `j` and `i` if `j` is the last index of `arr` and the elements from `i` to `j` are the same.

