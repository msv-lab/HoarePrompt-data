#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2·10^9.
def func_1(n):
    ways = 0
    for a in range(1, n // 2 + 1):
        for b in range(a, (n - a) // 2 + 1):
            if a != b and 2 * (a + b) == n:
                ways += 1
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 3, `ways` is the total number of pairs \((a, b)\) such that \(1 \leq a \leq \frac{n}{2}\), \(a \neq b\), and \(2 \times (a + b) = n\).
    return ways
    #`The program returns ways which is the total number of pairs (a, b) such that 1 ≤ a ≤ n/2, a ≠ b, and 2 * (a + b) = n`
#Overall this is what the function does:The function `func_1` accepts an integer `n` within the range 1 ≤ n ≤ 2·10^9 and returns the total number of pairs (a, b) such that 1 ≤ a ≤ n/2, a ≠ b, and 2 * (a + b) = n.

