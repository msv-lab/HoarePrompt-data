#State of the program right berfore the function call: arr is a list of integers where 1 <= arr[i] <= 500 for all 1 <= i < n, and n is an integer such that 2 <= n <= 500.
def func_1(arr, n):
    ans = [10 ** 9] * n
    i = n - 2
    while i >= 0:
        ans[i] = ans[i + 1] - arr[i]
        
        i -= 1
        
    #State: `i` is -1, `ans` is updated such that each element `ans[j]` for 0 <= j < n-1 is `ans[j+1] - arr[j]`.
    return ans
    #The program returns the list `ans` where each element `ans[j]` for 0 <= j < n-1 is calculated as `ans[j+1] - arr[j]`. The initial value of `i` is -1, but it does not affect the returned list `ans`.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers and an integer `n`. It returns a list `ans` where each element `ans[j]` for 0 <= j < n-1 is calculated as the difference between the next element in `ans` and the current element in `arr`. The final element of `ans` is always `10

