#State of the program right berfore the function call: arr is a list of integers where each integer a_i satisfies 1 <= a_i <= n, and n is the length of the list arr. The function is called once for each test case, and the sum of all n across test cases does not exceed 2 * 10^5. There are t test cases, where 1 <= t <= 10^4.
def func_1(arr):
    i = 0
    n = len(arr)
    j = len(arr) - 1
    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
        i += 1
        
    #State: `arr` is a list of integers where the first `k` elements are all equal (where `k` is the number of times the loop executed), and each integer `a_i` satisfies `1 <= a_i <= n`, `i` is `k`, `j` is `n - 1`, and `n` is the length of the list `arr`.
    while j > 0 and arr[j] == arr[j - 1]:
        j -= 1
        
    #State: `arr` is a list of integers where the first `k` elements are all equal, `i` is `k`, `j` is `0`, and `n` is the length of the list `arr`.
    if (arr[0] == arr[-1]) :
        return max(j - i - 1, 0)
        #The program returns 0
    #State: `arr` is a list of integers where the first `k` elements are all equal, `i` is `k`, `j` is `0`, and `n` is the length of the list `arr`. The first element of `arr` is not equal to the last element of `arr`.
    return max(min(n - i - 1, j), 0)
    #The program returns 0
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` where each integer is between 1 and the length of the list. It returns 0 regardless of the input.

