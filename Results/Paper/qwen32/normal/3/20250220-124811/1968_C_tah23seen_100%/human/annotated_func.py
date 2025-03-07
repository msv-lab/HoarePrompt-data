#State of the program right berfore the function call: arr is a list of integers where each integer x_i satisfies 1 <= x_i <= 500, and n is an integer such that 2 <= n <= 500 representing the number of elements in the array a (including the first element a_1 which is not provided in arr). The function is called for each test case, where the number of test cases t satisfies 1 <= t <= 10^4. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func_1(arr, n):
    ans = [10 ** 9] * n
    i = n - 2
    while i >= 0:
        ans[i] = ans[i + 1] - arr[i]
        
        i -= 1
        
    #State: `arr` is a list of integers where each integer \( x_i \) satisfies \( 1 \leq x_i \leq 500 \); `n` is an integer such that \( 2 \leq n \leq 500 \); `ans` is a list of `n` integers where `ans[0] = 10 - (arr[0] + arr[1] + ... + arr[n-2])`, `ans[1] = 10 - (arr[1] + ... + arr[n-2])`, ..., `ans[n-2] = 10 - arr[n-2]`, and `ans[n-1] = 10`; `i` is `-1`.
    return ans
    #The program returns a list `ans` of `n` integers where `ans[0] = 10 - (arr[0] + arr[1] + ... + arr[n-2])`, `ans[1] = 10 - (arr[1] + ... + arr[n-2])`, ..., `ans[n-2] = 10 - arr[n-2]`, and `ans[n-1] = 10`.
#Overall this is what the function does:The function `func_1` takes a list `arr` of integers and an integer `n`. It returns a list `ans` of `n` integers where each element `ans[i]` is calculated as `10 - (sum of elements in `arr` from index `i` to `n-2`), with `ans[n-1]` being `10`.

