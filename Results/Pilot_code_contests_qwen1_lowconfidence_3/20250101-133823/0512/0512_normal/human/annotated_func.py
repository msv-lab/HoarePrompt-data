#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 100, K is an integer such that 1 ≤ K ≤ 10^5, and a is a list of integers sorted in strictly increasing order such that 1 ≤ a_i ≤ K for all i in range N.
def func():
    input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    dp = [False] * (k + 1)
    for ai in a:
        dp[ai] = True
        
    #State of the program after the  for loop has been executed: `N` is at least 1, `a` is a non-empty list of integers sorted in strictly increasing order, `n` is an integer read from input, `k` is an integer read from input, `dp` is a list of length `k + 1` with all elements set to `True`.
    for i in xrange(max(a) + 1, k + 1):
        dp[i] = any(not dp[i - ai] for ai in a)
        
    #State of the program after the  for loop has been executed: dp is a list of length `k + 1` where `dp[i]` is `True` if and only if there exists at least one `ai` in `a` such that `dp[i - ai]` is `False`; `i` is `k + 1`; `a` is unchanged.
    os.write(1, 'First' if dp[k] else 'Second')
#Overall this is what the function does:The function accepts three parameters: `N`, `K`, and `a`. It reads `N` and `K` from input, where `N` is the number of elements in the list `a` and `K` is an integer such that `1 ≤ K ≤ 10^5`. The list `a` is a list of integers sorted in strictly increasing order such that `1 ≤ a_i ≤ K` for all `i` in range `N`. The function constructs a dynamic programming array `dp` of length `k + 1` initialized to `False`. It then sets `dp[ai]` to `True` for each element `ai` in `a`. After that, it iterates from `max(a) + 1` to `k` and updates `dp[i]` to `True` if there exists at least one `ai` in `a` such that `dp[i - ai]` is `False`. Finally, the function writes 'First' to the output if `dp[k]` is `True`, otherwise it writes 'Second'. Potential edge cases include when `N` is 1 and `a` contains only one element, or when `K` is much larger than the maximum value in `a`.

