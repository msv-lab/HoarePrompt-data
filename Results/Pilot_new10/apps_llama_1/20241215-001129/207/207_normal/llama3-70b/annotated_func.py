#State of the program right berfore the function call: m, a, and b are integers where 1 <= m <= 10^9, and 1 <= a, b <= 10^5.
def func():
    m, a, b = map(int, input().split())
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(m + 1):
        if i + a <= m:
            dp[i + a] += dp[i]
        
        if i - b >= 0:
            dp[i] += dp[i - b]
        
    #State of the program after the  for loop has been executed: `m` is an input integer, `a` is an input integer, `b` is an input integer, `dp` is a list of `m + 1` elements where `dp[i]` is the sum of `dp[i - b]` (if `i - b` is greater than or equal to 0) and `dp[i]` itself, and `dp[i + a]` (if `i + a` is less than or equal to `m`) is the sum of `dp[i + a]` itself and `dp[i]`, with `dp[0]` being 1.
    print(sum(dp))
#Overall this is what the function does:The function accepts three integer parameters `m`, `a`, and `b` as input from the user, initializes a dynamic programming list `dp` of size `m + 1`, updates `dp` based on `a` and `b`, and prints the sum of all elements in `dp`, effectively calculating and returning the sum of all reachable states in a sequence defined by `m`, `a`, and `b`.

