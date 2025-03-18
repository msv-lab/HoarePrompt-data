#State of the program right berfore the function call: arr is a list of integers where 1 <= arr[i] <= 500 for all 2 <= i <= n, and n is an integer such that 2 <= n <= 500.
def func_1(arr, n):
    ans = [10 ** 9] * n
    i = n - 2
    while i >= 0:
        ans[i] = ans[i + 1] - arr[i]
        
        i -= 1
        
    #State: `arr` is a list of integers where 1 <= arr[i] <= 500 for all 2 <= i <= n, `n` is an integer such that 2 <= n <= 500, `ans` is a list of length `n` where each element from `ans[0]` to `ans[n-2]` is updated to `ans[i + 1] - arr[i]`, and `i` is -1.
    return ans
    #The program returns a list `ans` of length `n` where each element from `ans[0]` to `ans[n-2]` is the difference between the next element in `ans` and the corresponding element in `arr`. The last element of `ans` remains unchanged.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers and an integer `n`. It returns a list `ans` of length `n` where each element from `ans[0]` to `ans[n-2]` is the difference between the next element in `ans` and the corresponding element in `arr`. The last element of `ans` remains unchanged, initialized to `10

