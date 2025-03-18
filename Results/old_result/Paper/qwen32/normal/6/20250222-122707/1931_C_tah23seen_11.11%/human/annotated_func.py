#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, and for each test case, the first integer n (1 ≤ n ≤ 2 · 10^5) is followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the elements of the array. The total sum of n across all test cases does not exceed 2 · 10^5.
def func_1(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        else:
            break
        
    #State: `i` and `j` such that either `arr[i] != arr[j]` or `i > j`.
    if (i > j) :
        return 0
        #The program returns 0
    #State: `i` and `j` such that `arr[i] != arr[j]` and `i` is not greater than `j`
    while arr[i] == arr[i + 1]:
        i += 1
        
    #State: `i` is a valid index such that `arr[i]` is not equal to `arr[i + 1]`, and `j` remains unchanged.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns the value of `j - i + 1`, where `i` is a valid index such that `arr[i]` is not equal to `arr[i + 1]`, and `j` remains unchanged and is not equal to `len(arr) - 1`.
    #State: `i` is a valid index such that `arr[i]` is not equal to `arr[i + 1]`, `j` remains unchanged, and `j` is equal to `len(arr) - 1`
    return j - i
    #The program returns the difference between the length of the array minus one (j) and the index i, where arr[i] is not equal to arr[i + 1].
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` as input, where the first element represents the number of test cases, and each subsequent test case consists of an integer `n` followed by `n` integers. The function returns 0 if all elements in the array of a test case are the same. Otherwise, it returns the length of the longest contiguous subarray where at least two consecutive elements are different.

