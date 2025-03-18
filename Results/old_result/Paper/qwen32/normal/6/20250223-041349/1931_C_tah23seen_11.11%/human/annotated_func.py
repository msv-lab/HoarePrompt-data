#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 1 <= a_i <= n, and the length of arr, n, satisfies 1 <= n <= 2 * 10^5. Additionally, there are t test cases (1 <= t <= 10^4) and the sum of n across all test cases does not exceed 2 * 10^5.
def func_1(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        else:
            break
        
    #State: The loop terminates with `i` and `j` such that `i` is either equal to `j` or `i` is greater than `j`. If `arr[i]` was equal to `arr[j]` for all iterations up to the point of termination, then `i` and `j` will be equal, pointing to the middle element if the array length is odd, or to the point just beyond the middle if the array length is even. If at any point `arr[i]` was not equal to `arr[j]`, the loop breaks, and `i` and `j` will be the indices where the elements first differ.
    if (i > j) :
        return 0
        #The program returns 0
    #State: The loop terminates with `i` and `j` such that `i` is equal to `j`. If `arr[i]` was equal to `arr[j]` for all iterations up to the point of termination, then `i` and `j` will be equal, pointing to the middle element if the array length is odd, or to the point just beyond the middle if the array length is even. If at any point `arr[i]` was not equal to `arr[j]`, the loop breaks, and `i` and `j` will be the indices where the elements first differ. Additionally, `i` is not greater than `j`.
    while arr[i] == arr[i + 1]:
        i += 1
        
    #State: `i` is the index where the first mismatch occurs, and `j` is `i + 1`.
    if (j != len(arr) - 1) :
        return j - i + 1
        #The program returns 2
    #State: `i` is the index where the first mismatch occurs, and `j` is `i + 1`. `j` is equal to `len(arr) - 1`.
    return j - i
    #The program returns 1
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` as input and returns 0 if the entire list is a palindrome, 1 if the list has a single mismatch at the end, and 2 if there is a mismatch that is not at the end.

