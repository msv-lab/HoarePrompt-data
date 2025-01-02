#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100000, and there are n subsequent lines containing integers ai such that 0 ≤ ai ≤ 109.
def func():
    n = input()
    a = [input() for i in xrange(n)]
    dp = [float('inf') for _ in xrange(n)]
    for i in xrange(n):
        dp[bisect.bisect_left(dp, a[i])] = a[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n-1`, `dp` is a list where each element at index `j` (where `0 <= j < n`) is the smallest value from the list `a` that is greater than or equal to `dp[j]` for all `j < k` where `k` is the index of the insertion. If the loop does not execute (`n` is 0), then `dp` remains a list of `n` elements, each set to infinity.
    for i in xrange(n):
        if dp[i] == float('inf'):
            print(i)
            break
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n`, `dp` is a list of length `n` with each element set to infinity.
#Overall this is what the function does:The function processes an input specifying the number of integers `n` (where `1 ≤ n ≤ 100000`), followed by `n` lines of space-separated integers `a_i` (where `0 ≤ a_i ≤ 10^9`). It then constructs a list `dp` of length `n`, where each element at index `j` is the smallest value from the list `a` that is greater than or equal to `dp[j]` for all `j < k`, where `k` is the index of the insertion. If no such value can be found (i.e., `dp[j]` remains `float('inf')`), the function prints the index `j` and breaks out of the loop. If the loop completes without finding any such value, the function prints `n`.

