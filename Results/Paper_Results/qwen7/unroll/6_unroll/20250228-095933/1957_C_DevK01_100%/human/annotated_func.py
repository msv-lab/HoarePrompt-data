#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5; k is an integer such that 0 ≤ k ≤ n; for each test case, r_i and c_i are integers such that 1 ≤ r_i, c_i ≤ n, and no two rooks attack each other based on the described rules.
def func_1(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        dp += [(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)]
        
        dp.pop(0)
        
    #State: Output State: `dp` is a list of length `n`, where each element is calculated based on the recurrence relation `(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)` for `i` ranging from 2 to `n`, with the initial values `[1, 1]`.
    return dp[-1]
    #The program returns the last element of the list `dp` which is calculated based on the recurrence relation \((dp[-1] + 2 * (i - 1) * dp[-2]) \% (7 + 10^9)\) for \(i\) ranging from 2 to \(n\), starting with the initial values \([1, 1]\).
#Overall this is what the function does:The function accepts an integer `n` and returns the last element of the list `dp` calculated using the recurrence relation \((dp[-1] + 2 * (i - 1) * dp[-2]) \% (7 + 10^9)\) for \(i\) ranging from 2 to \(n\), starting with the initial values \([1, 1]\).

