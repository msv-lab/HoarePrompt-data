#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 100, K is an integer such that 1 ≤ K ≤ 10^5, and a is a list of integers representing A such that 1 ≤ a[i] ≤ K and a[i] < a[i+1] for all i.
def func():
    input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    dp = [False] * (k + 1)
    for ai in a:
        dp[ai] = True
        
    #State of the program after the  for loop has been executed: `N` is an integer such that \(1 \leq N \leq 100\), `K` is an integer such that \(1 \leq K \leq 10^5\), `a` is a list of integers, `dp` is a list of length `K + 1` with all elements initialized to `False` except for `dp[ai]` which is `True` for each `ai` in `a`.
    for i in xrange(max(a) + 1, k + 1):
        dp[i] = any(not dp[i - ai] for ai in a)
        
    #State of the program after the  for loop has been executed: `max(a) + 1` is less than or equal to `k + 1`, `N` is an integer such that \(1 \leq N \leq 100\), `K` is an integer such that \(1 \leq K \leq 10^5\), `a` is a list of integers, `dp` is a list of length `K + 1` with `dp[i]` being `True` for all `i` in the range `[max(a) + 1, k + 1]` if it is possible to form `i` using the values in `a`, otherwise `dp[i]` is `False`.
    os.write(1, 'First' if dp[k] else 'Second')
#Overall this is what the function does:The function takes a list `a` of integers and two integers `N` and `K` as input, where `N` is the number of elements in `a`, `K` is the upper limit for the values in `a`, and `a` is sorted in increasing order. It constructs a dynamic programming array `dp` of length `K + 1` where `dp[i]` indicates whether it is possible to form the integer `i` using the values in `a`. After filling the `dp` array, it checks if it is possible to form the integer `K` using the values in `a`. If `dp[K]` is `True`, it writes "First" to standard output; otherwise, it writes "Second". This function essentially determines which player wins a game where players take turns removing elements from `a` and the player who cannot make a move loses.

