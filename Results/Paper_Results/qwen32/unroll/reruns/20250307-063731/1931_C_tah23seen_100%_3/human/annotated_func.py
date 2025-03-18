#State of the program right berfore the function call: arr is a list of integers where each integer represents the size of the array for a test case, followed by the array elements which are integers in the range [1, n] for each test case. The first element of arr is the number of test cases t (1 ≤ t ≤ 10^4). For each test case, the first integer is n (1 ≤ n ≤ 2 · 10^5), the size of the array, and the next n integers are the elements of the array. The sum of n for all test cases does not exceed 2 · 10^5.
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: i=0, n=original length of arr, j=len(arr) - 1.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: i=0, n=original length of arr, j=index of the first element from the end that is not the same as the one before it.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum of (j - i - 1, 0)
    #State: i=0, n=original length of arr, j=index of the first element from the end that is not the same as the one before it, and the first element of arr is not the same as the last element of arr
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum of 0 and the minimum of (n - i - 1) and j
#Overall this is what the function does:The function `func_1` processes a list of integers representing multiple test cases. Each test case starts with an integer `n` indicating the size of the array, followed by `n` integers representing the elements of the array. For each test case, the function calculates and returns the maximum of two values: the maximum of `(j - i - 1, 0)` if the first and last elements of the array are the same, or the maximum of `0` and the minimum of `(n - i - 1)` and `j` if they are different. Here, `i` is the index of the first element from the start that is not the same as the one after it, and `j` is the index of the first element from the end that is not the same as the one before it.

