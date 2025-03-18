#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, followed by t pairs of lines where the first line of each pair contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the size of the array, and the second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the elements of the array. The sum of n for all test cases does not exceed 2 · 10^5.
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: i is 0, n is 1 + 2 * t, j is 2 * t, arr remains the same.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: Output State:
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum value between the number of elements between indices `i` and `j` minus one, and 0. Given the information, the returned value is at least 0.
    #State: Output State: `arr` is a list of elements, and the first element of `arr` is not equal to the last element of `arr`.
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum of 0 and the minimum of (n - i - 1) and j.
#Overall this is what the function does:The function processes a list of integers where the first element represents the number of test cases. For each test case, it calculates and returns the maximum value between the number of elements between indices `i` and `j` minus one and 0, or the maximum of 0 and the minimum of (n - i - 1) and j, depending on whether the first and last elements of the array are equal.

