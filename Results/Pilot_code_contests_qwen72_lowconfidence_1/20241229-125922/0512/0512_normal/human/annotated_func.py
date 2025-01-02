#State of the program right berfore the function call: N and K are integers such that 1 ≤ N ≤ 100 and 1 ≤ K ≤ 10^5. a is a list of N unique integers where 1 ≤ a_1 < a_2 < ... < a_N ≤ K.
def func():
    input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    dp = [False] * (k + 1)
    for ai in a:
        dp[ai] = True
        
    #State of the program after the  for loop has been executed: `N` and `K` are integers such that 1 ≤ N ≤ 100 and 1 ≤ K ≤ 10^5, `n` is an integer read from standard input, `k` is an integer read from standard input, `a` is a list of integers provided by user input, `dp` is a list of length `k + 1` where each element at index `i` is `True` if `i` is present in `a` and `False` otherwise.
    for i in xrange(max(a) + 1, k + 1):
        dp[i] = any(not dp[i - ai] for ai in a)
        
    #State of the program after the  for loop has been executed: `N` and `K` are integers such that 1 ≤ N ≤ 100 and 1 ≤ K ≤ 10^5, `n` is an integer read from standard input, `k` is an integer read from standard input, `a` is a list of integers provided by user input, `dp` is a list of length `k + 1` where each element at index `i` is `True` if `i` is present in `a` or if there exists at least one `ai` in `a` such that `dp[i - ai]` is `False`, and `False` otherwise for `i` in the range `[max(a) + 1, k]`, and `False` for `i` in the range `[0, max(a)]`.
    os.write(1, 'First' if dp[k] else 'Second')
#Overall this is what the function does:The function reads two integers `N` and `K` from standard input, followed by a list `a` of `N` unique integers. It then initializes a list `dp` of length `K + 1` with all elements set to `False`. For each integer `ai` in `a`, it sets `dp[ai]` to `True`. Afterward, for each integer `i` from `max(a) + 1` to `K`, it sets `dp[i]` to `True` if there exists at least one `ai` in `a` such that `dp[i - ai]` is `False`. Finally, it writes 'First' to standard output if `dp[K]` is `True`, otherwise it writes 'Second'. The function does not return any value. Edge cases include scenarios where `K` is less than or equal to the maximum value in `a`, or when `a` contains only one element.

