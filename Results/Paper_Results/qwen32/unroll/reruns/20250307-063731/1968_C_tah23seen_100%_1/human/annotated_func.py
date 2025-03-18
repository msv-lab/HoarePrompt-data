#State of the program right berfore the function call: arr is a list of integers where 1 <= len(arr) <= 499 and 1 <= arr[i] <= 500 for all 0 <= i < len(arr). n is an integer such that n = len(arr) + 1 and 2 <= n <= 500.
def func_1(arr, n):
    ans = [10 ** 9] * n
    i = n - 2
    while i >= 0:
        ans[i] = ans[i + 1] - arr[i]
        
        i -= 1
        
    #State: 
    return ans
    #The program returns the value of `ans`
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` and an integer `n` (where `n` is the length of `arr` plus one) and returns a list `ans` of length `n`. The list `ans` is constructed such that each element at index `i` (except the last one) is the result of subtracting the corresponding element in `arr` from the element at index `i + 1` in `ans`. The initial value of the last element in `ans` is set to \(10^9\).

