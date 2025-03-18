#State of the program right berfore the function call: arr is a list of n-1 integers where each integer x_i satisfies 1 <= x_i <= 500, and n is an integer such that 2 <= n <= 500. The function is called for each test case, where the number of test cases t satisfies 1 <= t <= 10^4, and the sum of all n over all test cases does not exceed 2 * 10^5.
def func_1(arr, n):
    ans = [0] * n
    ans[0] = arr[0] + 1
    for i in range(n - 2):
        ans[i + 1] = arr[i] + ans[i]
        
        if ans[i + 1] < arr[i + 1]:
            while ans[i + 1] <= arr[i + 1]:
                ans[i + 1] += ans[i]
        
    #State: - `ans[0]` remains `arr[0] + 1`.
    #- For `i` from `1` to `n-2`, `ans[i]` will be the smallest number greater than `arr[i]` that is a multiple of `ans[i-1]` plus `arr[i-1]`.
    #
    #Thus, the output state can be described as follows:
    #
    #Output State:
    ans[-1] = ans[-2] + arr[-1]
    return ans
    #The program returns the list `ans` where `ans[0]` is `arr[0] + 1`, for each `i` from `1` to `n-2`, `ans[i]` is the smallest number greater than `arr[i]` that is a multiple of `ans[i-1]` plus `arr[i-1]`, and `ans[-1]` is `ans[-2] + arr[-1]`.
#Overall this is what the function does:The function `func_1` takes a list `arr` of `n-1` integers and an integer `n`, and returns a list `ans` of `n` integers. The first element of `ans` is `arr[0] + 1`. For each subsequent element from index `1` to `n-2`, `ans[i]` is the smallest number greater than `arr[i]` that is a multiple of `ans[i-1]` plus `arr[i-1]`. The last element `ans[-1]` is the sum of `ans[-2]` and `arr[-1]`.

