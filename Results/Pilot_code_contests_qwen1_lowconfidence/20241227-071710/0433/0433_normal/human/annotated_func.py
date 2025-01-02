#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100000, and a list A = [a0, a1, ..., an-1] where each ai is an integer such that 0 ≤ ai ≤ 109.
def func():
    n = input()
    a = [input() for i in xrange(n)]
    dp = [float('inf') for _ in xrange(n)]
    for i in xrange(n):
        dp[bisect.bisect_left(dp, a[i])] = a[i]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 100000, `a` is a list of `n` integers such that 0 ≤ ai ≤ 10^9 for each `i` where 0 ≤ i < n, `dp` is a list of `n` elements where the first k elements (k being the length of the unique sorted subsequence of `a`) are the sorted unique elements of `a`, and the rest are `float('inf')`, `i` is `n`
    for i in xrange(n):
        if dp[i] == float('inf'):
            print(i)
            break
        
    #State of the program after the  for loop has been executed: Output State: `i` is the index of the first non-`inf` element in `dp` or `n-1` if all elements in `dp` are `float('inf')`.
#Overall this is what the function does:The function accepts a list \( A \) of integers \( a_i \) where the length of the list is \( n \) such that \( 1 \leq n \leq 100000 \), and each element \( a_i \) is an integer such that \( 0 \leq a_i \leq 10^9 \). The function computes the length of the longest strictly increasing subsequence in the list \( A \) and prints the index of the first position where the dynamic programming array \( dp \) contains `float('inf')`. If all elements in \( dp \) are `float('inf')`, it prints \( n-1 \).

