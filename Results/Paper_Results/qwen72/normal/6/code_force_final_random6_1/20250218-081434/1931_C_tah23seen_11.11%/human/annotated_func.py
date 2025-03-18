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
        
    #State: If `arr` is a palindrome (meaning it reads the same forwards and backwards), then `i` is len(arr) // 2 and `j` is len(arr) // 2 - 1 if the length of `arr` is even, or `i` is (len(arr) // 2) + 1 and `j` is len(arr) // 2 - 1 if the length of `arr` is odd. Otherwise, `i` and `j` remain at the positions where `arr[i]` is not equal to `arr[j]`.
    if (i > j) :
        return 0
        #The program returns 0.
    #State: If `arr` is a palindrome (meaning it reads the same forwards and backwards), then `i` is len(arr) // 2 and `j` is len(arr) // 2 - 1 if the length of `arr` is even, or `i` is (len(arr) // 2) + 1 and `j` is len(arr) // 2 - 1 if the length of `arr` is odd. Otherwise, `i` and `j` remain at the positions where `arr[i]` is not equal to `arr[j]`. Additionally, `i` is less than or equal to `j`.
    while arr[i] == arr[i + 1]:
        i += 1
        
    #State: `arr[i]` is no longer equal to `arr[i + 1]`, and `i` is increased by the number of consecutive equal elements starting from the initial `i`.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns the difference between `j` and `i`, plus 1. Here, `i` has been increased by the number of consecutive equal elements starting from the initial `i`, and `j` is not equal to the length of `arr` minus 1.
    #State: *`arr[i]` is no longer equal to `arr[i + 1]`, and `i` is increased by the number of consecutive equal elements starting from the initial `i`. `j` is equal to `len(arr) - 1`.
    return j - i
    #The program returns the difference between `j` and `i`, where `j` is `len(arr) - 1` and `i` is increased by the number of consecutive equal elements starting from the initial `i`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and checks if the list is a palindrome. If `arr` is a palindrome, the function returns 0. If `arr` is not a palindrome, the function finds the first pair of non-matching elements from the start and end of the list, then increments the starting index `i` to skip over any consecutive equal elements. The function returns the length of the subarray from the updated `i` to `j` (inclusive), or the length from `i` to the end of the list if `j` is the last index.

