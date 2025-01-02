#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 100, K is an integer such that 1 ≤ K ≤ 10^5, and a is a list of integers representing the set A where 1 ≤ a_1 < a_2 < ... < a_N ≤ K.
def func():
    input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    dp = [False] * (k + 1)
    for ai in a:
        dp[ai] = True
        
    #State of the program after the  for loop has been executed: N is an integer such that 1 ≤ N ≤ 100, K is an integer such that 1 ≤ K ≤ 10^5, a is a non-empty list of integers, n is the first integer read from the input, k is the second integer read from the input, dp is a list of length k + 1, dp[ai] is True for each ai in a.
    for i in xrange(max(a) + 1, k + 1):
        dp[i] = any(not dp[i - ai] for ai in a)
        
    #State of the program after the  for loop has been executed: `dp[i]` is set to `any(not dp[i - ai] for ai in a)` for all valid indices `i` in the range `[max(a) + 1, k]`, `a` is the list of integers, and `dp` is a list of length `k + 1`.
    os.write(1, 'First' if dp[k] else 'Second')
#Overall this is what the function does:The function accepts two integers `n` and `k`, and a list of integers `a` representing a set A where 1 ≤ a_1 < a_2 < ... < a_N ≤ K, with constraints 1 ≤ N ≤ 100 and 1 ≤ K ≤ 10^5. It constructs a dynamic programming (DP) array `dp` of length `k + 1` initialized to `False`. It then marks the positions in `dp` corresponding to elements in `a` as `True`. After that, it fills the rest of the `dp` array based on the subset sum problem, determining whether each value up to `k` can be formed using the elements in `a`. Finally, it writes 'First' to standard output if `dp[k]` is `True`, indicating that the value `k` can be formed, otherwise it writes 'Second'. Potential edge cases include when `a` contains all values from 1 to K, in which case `dp[k]` will always be `True`. If `k` is less than the maximum element in `a`, `dp[k]` will remain `False`. The function does not handle cases where the input constraints are violated.

