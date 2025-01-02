#State of the program right berfore the function call: N and M are integers such that 2 ≤ N, M ≤ 50, and a_i, b_i are integers satisfying 1 ≤ a_i, b_i ≤ N and a_i ≠ b_i for all 1 ≤ i ≤ M.
def func():
    n, m = map(int, raw_input().split())
    count = [0] * n
    for i in xrange(m):
        a, b = map(int, raw_input().split())
        
        count[a - 1] += 1
        
        count[b - 1] += 1
        
    #State of the program after the  for loop has been executed: `m` is a non-negative integer, `count` is a list of length `n` where each element `count[i]` (0-indexed) represents the number of times `i + 1` appears in the inputs, `N` is `n`, `M` is `m`.
    for i in xrange(n):
        print(count[i])
        
    #State of the program after the  for loop has been executed: `m` is a non-negative integer, `count` is a list of length `n` where each element `count[i]` (0-indexed) represents the number of times `i + 1` appears in the inputs, `N` is `n`, `M` is `m`, and `i` is `n - 1`; all elements `count[0]` through `count[n-1]` are printed.
#Overall this is what the function does:The function takes two integers \(N\) and \(M\) as input, where \(2 \leq N, M \leq 50\), and processes \(M\) pairs of integers \((a, b)\) such that \(1 \leq a, b \leq N\) and \(a \neq b\). It counts the number of times each integer from 1 to \(N\) appears in these pairs. Specifically, it increments the count for both \(a-1\) and \(b-1\) in a list `count` of length \(N\). After processing all pairs, it prints the count of appearances for each integer from 1 to \(N\). The function does not return any value; instead, it modifies and prints the `count` list. Potential edge cases include when \(N\) or \(M\) is exactly 2, and when the input values for \(a\) and \(b\) are at the boundary conditions (i.e., 1 or \(N\)). The function also assumes valid input within the specified range.

