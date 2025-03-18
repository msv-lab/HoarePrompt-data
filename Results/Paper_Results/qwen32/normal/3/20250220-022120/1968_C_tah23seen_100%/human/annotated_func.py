#State of the program right berfore the function call: arr is a list of integers where each element x_i satisfies 1 \le x_i \le 500, and n is an integer such that 2 \le n \le 500 representing the length of the list arr plus one. The function is called once for each test case, and there are t test cases in total where 1 \le t \le 10^4. The sum of all n values across all test cases does not exceed 2 \cdot 10^5.
def func_1(arr, n):
    ans = [10 ** 9] * n
    i = n - 2
    while i >= 0:
        ans[i] = ans[i + 1] - arr[i]
        
        i -= 1
        
    #State: `arr` is a list of integers where each element \( x_i \) satisfies \( 1 \leq x_i \leq 500 \); `n` is an integer such that \( 2 \leq n \leq 500 \); `ans` is a list of `n` elements where `ans[i]` is `10 - arr[i]` for `i` from `0` to `n-2` and `ans[n-1]` is `10`; `i` is `-1`.
    return ans
    #The program returns a list `ans` of `n` elements where `ans[i]` is `10 - arr[i]` for `i` from `0` to `n-2` and `ans[n-1]` is `10`.
#Overall this is what the function does:The function accepts a list `arr` of integers where each element `x_i` satisfies 1 ≤ `x_i` ≤ 500, and an integer `n` such that 2 ≤ `n` ≤ 500 representing the length of the list `arr` plus one. It returns a list `ans` of `n` elements where `ans[i]` is `10 - arr[i]` for `i` from `0` to `n-2` and `ans[n-1]` is `10`.

