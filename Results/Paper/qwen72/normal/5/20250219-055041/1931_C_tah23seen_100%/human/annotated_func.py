#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr).
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: `arr` is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr). `i` is the index of the first element in `arr` that is not equal to `arr[i + 1]` or `i` is equal to `len(arr) - 1` if all elements are equal. `n` is equal to the length of `arr` and `n` must be greater than 1. `j` is equal to `n - 1`.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: `arr` is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr). `i` is the index of the first element in `arr` that is not equal to `arr[i + 1]` or `i` is equal to `len(arr) - 1` if all elements are equal. `n` is equal to the length of `arr` and `n` must be greater than 1. `j` is the largest index such that `arr[j]` is not equal to `arr[j - 1]` and `j` is greater than 0, or `j` is 0 if all elements in `arr` are equal.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum of 0 and the difference between `j` and `i` minus 1, where `j` is the largest index such that `arr[j]` is not equal to `arr[j - 1]` and `i` is the index of the first element in `arr` that is not equal to `arr[i + 1]`. If all elements in `arr` are equal, `j` is 0 and `i` is `len(arr) - 1`.
    #State: `arr` is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr). `i` is the index of the first element in `arr` that is not equal to `arr[i + 1]` or `i` is equal to `len(arr) - 1` if all elements are equal. `n` is equal to the length of `arr` and `n` must be greater than 1. `j` is the largest index such that `arr[j]` is not equal to `arr[j - 1]` and `j` is greater than 0, or `j` is 0 if all elements in `arr` are equal. Additionally, `arr[0]` is not equal to `arr[-1]`.
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum value between 0 and the minimum of (n - i - 1) and j, where n is the length of the list `arr`, i is the index of the first element in `arr` that is not equal to `arr[i + 1]` or `len(arr) - 1` if all elements are equal, and j is the largest index such that `arr[j]` is not equal to `arr[j - 1]` and `j` is greater than 0, or 0 if all elements in `arr` are equal.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and returns an integer. It calculates the maximum of 0 and the difference between the largest index `j` of a non-repeating element from the end of the list and the first index `i` of a non-repeating element from the start of the list, minus 1. If all elements in `arr` are equal, it returns the maximum of 0 and the minimum of the length of the list minus the first index `i` minus 1, and the largest index `j` of a non-repeating element from the end, which is 0 in this case.

