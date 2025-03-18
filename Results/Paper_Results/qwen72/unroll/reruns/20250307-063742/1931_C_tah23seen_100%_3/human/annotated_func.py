#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= len(arr).
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: `i` is the index of the first element in `arr` that is different from its next element, or `i` is equal to `len(arr) - 1` if all elements in `arr` are the same. `j` remains `n - 1`.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: `i` remains the same, and `j` is the index of the last element in `arr` that is different from its previous element, or `j` is `0` if all elements in `arr` are the same.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum value between `j - i - 1` and `0`, where `i` remains the same, and `j` is the index of the last element in `arr` that is different from its previous element, or `j` is `0` if all elements in `arr` are the same. Additionally, the first element of `arr` is equal to the last element of `arr`.
    #State: `i` remains the same, and `j` is the index of the last element in `arr` that is different from its previous element, or `j` is `0` if all elements in `arr` are the same. Additionally, the first element of `arr` is not equal to the last element of `arr`.
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum value between 0 and the minimum value of (n - i - 1) and j, where n is the length of the list `arr`, `i` remains the same, and `j` is the index of the last element in `arr` that is different from its previous element, or `j` is `0` if all elements in `arr` are the same. Additionally, the first element of `arr` is not equal to the last element of `arr`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and returns an integer. It determines the indices `i` and `j` such that `i` is the index of the first element in `arr` that is different from its next element, and `j` is the index of the last element in `arr` that is different from its previous element. If the first and last elements of `arr` are the same, the function returns the maximum of `j - i - 1` and `0`. If the first and last elements are different, the function returns the maximum of `0` and the minimum of `(n - i - 1)` and `j`, where `n` is the length of `arr`.

