#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 2 * 10^5 and 1 <= arr[i] <= len(arr).
def func_1(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        else:
            break
        
    #State: If the loop completes all iterations, then `i` is `len(arr) // 2` and `j` is `len(arr) // 2 - 1` if `len(arr)` is even, or `i` is `len(arr) // 2 + 1` and `j` is `len(arr) // 2 - 1` if `len(arr)` is odd. If the loop breaks early, then `i` and `j` are the indices where `arr[i]` is not equal to `arr[j]`.
    if (i > j) :
        return 0
        #The program returns 0.
    #State: If the loop completes all iterations, then `i` is `len(arr) // 2` and `j` is `len(arr) // 2 - 1` if `len(arr)` is even, or `i` is `len(arr) // 2 + 1` and `j` is `len(arr) // 2 - 1` if `len(arr)` is odd. If the loop breaks early, then `i` and `j` are the indices where `arr[i]` is not equal to `arr[j]`. Additionally, `i` is less than or equal to `j`.
    while arr[i] == arr[i + 1]:
        i += 1
        
    #State: `i` is the index where `arr[i]` is not equal to `arr[i + 1]` or `i` is equal to `len(arr) - 1`. `j` remains unchanged.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns the difference between `j` and `i`, plus 1.
    #State: *`i` is the index where `arr[i]` is not equal to `arr[i + 1]` or `i` is equal to `len(arr) - 1`. `j` remains unchanged, and `j` is equal to `len(arr) - 1`.
    return j - i
    #The program returns the difference between `j` and `i`, where `j` is equal to `len(arr) - 1` and `i` is the index where `arr[i]` is not equal to `arr[i + 1]` or `i` is equal to `len(arr) - 1`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and checks if the list is a palindrome. If the list is a palindrome, it returns 0. If the list is not a palindrome, it finds the first pair of indices `i` and `j` where `arr[i]` is not equal to `arr[j]` and returns the difference `j - i + 1`. If the loop breaks and `j` is the last index of the list, it returns the difference `j - i`.

