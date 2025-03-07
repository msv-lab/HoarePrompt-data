#State of the program right berfore the function call: arr is a list of integers where the length of the list is n (1 <= n <= 2 * 10^5), and each element a_i satisfies 1 <= a_i <= n.
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: Output State: `i` is the length of `arr`; `j` is the length of `arr` - 1; all consecutive elements in `arr` from index 0 to `i-1` must be equal.
    #
    #This means that after the loop has executed all its iterations, `i` will be equal to the length of `arr`, indicating that the loop has processed all elements in `arr` as long as they were consecutive duplicates. The variable `j` remains unchanged at the length of `arr` - 1, and all elements from `arr[0]` to `arr[i-1]` (which is effectively all elements in `arr`) must be identical.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: The value of `i` is the length of `arr`, `j` is 0, and all elements in `arr` are identical.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum value between 0 and the difference between j and i minus 1, given that j is 0 and i is the length of arr.
    #State: The value of `i` is the length of `arr`, `j` is 0, and not all elements in `arr` are identical
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum value between the minimum of (the length of `arr` minus `i` minus 1) and `j`, and 0.
#Overall this is what the function does:The function accepts a list of integers `arr` and returns a non-negative integer. It first checks if all elements in `arr` are identical by verifying that `arr[0]` equals `arr[-1]`. If true, it calculates and returns the maximum value between 0 and the difference between `j` and `i` minus one, where `i` is the length of `arr` and `j` is initially the last index of `arr`. If false, it returns the maximum value between the minimum of (the length of `arr` minus `i` minus 1) and `j`, and 0.

