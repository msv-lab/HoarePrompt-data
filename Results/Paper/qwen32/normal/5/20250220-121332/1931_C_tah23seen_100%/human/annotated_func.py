#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, and for each test case, the first integer n (1 ≤ n ≤ 2 · 10^5) is followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the elements of the array. The sum of n across all test cases does not exceed 2 · 10^5.
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: `arr` is a list of integers, `i` is the index of the first element that is different from the previous one or `len(arr) - 1` if all elements are the same, `n` is the length of `arr`, and `j` is `len(arr) - 1`.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: `arr` remains the same, `i` remains the same, `n` remains the same, and `j` is the index of the first element from the end that is different from the previous element, or 0 if all elements are the same.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns the maximum of (j - i - 1) and 0, where j is the index of the first element from the end that is different from the previous element, or 0 if all elements are the same.
    #State: `arr` remains the same, `i` remains the same, `n` remains the same, and `j` is the index of the first element from the end that is different from the previous element, or 0 if all elements are the same. Additionally, the first element of `arr` is not equal to the last element of `arr`.
    return max(min(n - i - 1, j), 0)
    #The program returns the maximum of `n - i - 1` and `j`.
#Overall this is what the function does:The function accepts a list of integers `arr` where the first element `t` represents the number of test cases. For each test case, the first integer `n` is followed by `n` integers representing the elements of the array. The function returns the maximum length of a subarray that does not include the first and last elements if they are the same, or the maximum length of a subarray starting from the first element or ending at the last element, excluding the first or last element respectively, if the first and last elements are different. If all elements in a test case are the same, it returns 0.

