#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 0 ≤ k ≤ n; for each test case, r_i and c_i are integers such that 1 ≤ r_i, c_i ≤ n and the moves are valid according to the problem description.
def func_1(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        dp += [(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)]
        
        dp.pop(0)
        
    #State: Output State: The loop will continue to execute until `i` reaches `n + 1`. After all iterations, `dp` will contain `n - 1` elements. Each element in `dp` will be calculated based on the formula `(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10^9)` for `i` from 2 to `n`, with the first two elements being 1.
    #
    #In more detail, after the loop completes all its iterations, `dp` will look like this:
    #- `dp[0]` will be 1,
    #- `dp[1]` will be 3 (since the second element is calculated as `(dp[0] + 2 * 1 * 0) % (7 + 10^9) = 1 + 0 = 1`, but the loop starts from index 1),
    #- Each subsequent element will follow the given recurrence relation.
    #
    #The final state of `dp` will be a list of length `n - 1`, with each element computed based on the previous two elements modulo \(7 \times 10^9 + 7\).
    return dp[-1]
    #The program returns the last element of the list `dp` which is calculated based on the recurrence relation `(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10^9)` for `i` from 2 to `n`, starting with `dp[0] = 1` and `dp[1] = 3`.
#Overall this is what the function does:The function accepts an integer `n` and calculates the last element of a list `dp` based on a specific recurrence relation. The list `dp` is initialized with the first two elements as 1 and 3. For each integer `i` from 2 to `n`, the next element in `dp` is computed using the formula `(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10^9)`. After all iterations, the function returns the last element of the list `dp`.

