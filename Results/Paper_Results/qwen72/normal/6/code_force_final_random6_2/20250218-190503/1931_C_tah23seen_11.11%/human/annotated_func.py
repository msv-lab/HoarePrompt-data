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
        
    #State: The loop will terminate when `i` is greater than `j` or when `arr[i]` is not equal to `arr[j]`. If the loop completes without breaking, `i` will be equal to `j + 1` or `i` will be equal to `j` if the length of `arr` is odd. If the loop breaks, `i` and `j` will be at the positions where `arr[i]` is not equal to `arr[j]`. The list `arr` remains unchanged.
    if (i > j) :
        return 0
        #The program returns 0.
    #State: The loop will terminate when `i` is greater than `j` or when `arr[i]` is not equal to `arr[j]`. If the loop completes without breaking, `i` will be equal to `j + 1` or `i` will be equal to `j` if the length of `arr` is odd. If the loop breaks, `i` and `j` will be at the positions where `arr[i]` is not equal to `arr[j]`. The list `arr` remains unchanged. Additionally, `i` is less than or equal to `j`.
    while arr[i] == arr[i + 1]:
        i += 1
        
    #State: `i` is increased by the number of consecutive duplicate elements starting from the initial `i`, `i` is less than or equal to `j`, and `arr[i]` is either not equal to `arr[i + 1]` or `i` is greater than `j`.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns the number of elements from index `i` to index `j` inclusive in the list `arr`, where `i` is less than or equal to `j`, and `j` is not the last index of `arr`.
    #State: *`i` is increased by the number of consecutive duplicate elements starting from the initial `i`, `i` is less than or equal to `j`, and `arr[i]` is either not equal to `arr[i + 1]` or `i` is greater than `j`. Additionally, `j` is equal to `len(arr) - 1`.
    return j - i
    #The program returns the difference between `j` and `i`, where `j` is the last index of the list `arr` and `i` is the index after being increased by the number of consecutive duplicate elements starting from the initial `i`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and checks if the list is a palindrome. If the list is a palindrome, it returns 0. If the list is not a palindrome, it returns the length of the longest segment of the list that is not a palindrome, starting from the first mismatching pair of elements. If the mismatch is found at the end of the list, it returns the difference between the last index and the index of the first element in the mismatching segment. The list `arr` remains unchanged.

