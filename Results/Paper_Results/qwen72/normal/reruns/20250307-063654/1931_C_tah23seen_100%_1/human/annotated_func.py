#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr).
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: `arr` is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr); `i` is the index of the first element in `arr` that is not equal to its next element, or `i` is `len(arr) - 1` if all elements are equal; `n` is the length of `arr` and `n` must be greater than or equal to `i + 1`; `j` is `n - 1`.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: `arr` is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr); `i` is the index of the first element in `arr` that is not equal to its next element, or `i` is `len(arr) - 1` if all elements are equal; `n` is the length of `arr` and `n` must be greater than or equal to `i + 1`; `j` is the largest index such that `arr[j] == arr[j - 1]` and `j > 0`, or `j` is 0 if no such index exists.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum value between 0 and (j - i - 1), where `j` is the largest index such that `arr[j] == arr[j - 1]` and `j > 0`, or `j` is 0 if no such index exists, and `i` is the index of the first element in `arr` that is not equal to its next element, or `i` is `len(arr) - 1` if all elements are equal.
    #State: *`arr` is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr); `i` is the index of the first element in `arr` that is not equal to its next element, or `i` is `len(arr) - 1` if all elements are equal; `n` is the length of `arr` and `n` must be greater than or equal to `i + 1`; `j` is the largest index such that `arr[j] == arr[j - 1]` and `j > 0`, or `j` is 0 if no such index exists. Additionally, the first element of `arr` is not equal to the last element of `arr`.
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum of 0 and the minimum of (`n - i - 1`, `j`), where `n` is the length of `arr`, `i` is the index of the first element in `arr` that is not equal to its next element, or `len(arr) - 1` if all elements are equal, and `j` is the largest index such that `arr[j] == arr[j - 1]` and `j > 0`, or 0 if no such index exists.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and returns a non-negative integer. It calculates the maximum value between 0 and a difference based on the indices of specific elements in the list. Specifically, it returns the maximum of 0 and (j - i - 1) if the first and last elements of `arr` are equal, or the maximum of 0 and the minimum of (n - i - 1, j) otherwise. Here, `i` is the index of the first element in `arr` that is not equal to its next element, or `len(arr) - 1` if all elements are equal; `j` is the largest index such that `arr[j] == arr[j - 1]` and `j > 0`, or 0 if no such index exists; and `n` is the length of `arr`.

