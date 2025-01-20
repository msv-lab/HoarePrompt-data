#State of the program right berfore the function call: n and m are non-negative integers such that 0 <= n, m <= 1,000,000 and n + m > 0.
def func():
    n, m = map(int, input().split())

towers = set()
    for i in range(1, n + 1):
        towers.add(i * 2)
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` must be at least 1, `towers` is a set containing {2, 4, ..., 2 * n}`.
    #
    #### Explanation:
    #1.
    for i in range(1, m + 1):
        towers.add(i * 3)
        
    #State of the program after the  for loop has been executed: Output State: `i` is `n + m`, `n` must be at least 1, `m` must be non-negative, and `towers` contains `{2, 4, ..., 2 * n}` along with `{3 * i | i in range(1, m + 1)}`.
    print(max(towers))
#Overall this is what the function does:The function reads two non-negative integers \( n \) and \( m \) (where \( 0 \leq n, m \leq 1,000,000 \) and \( n + m > 0 \)) from standard input. It then creates a set named `towers` which initially contains the first \( n \) even numbers (i.e., \(\{2, 4, 6, \ldots, 2n\}\)). Next, it adds to this set the first \( m \) multiples of 3 (i.e., \(\{3, 6, 9, \ldots, 3m\}\)). Finally, it prints the maximum value present in the `towers` set. Potential edge cases include when either \( n \) or \( m \) is zero, but both cannot be zero simultaneously due to the condition \( n + m > 0 \). If both \( n \) and \( m \) are zero, the function will still read the values and initialize an empty set, resulting in the output being 0.

