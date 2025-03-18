#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 2 * 10^9.
def func_1(n):
    ways = 0
    for a in range(1, n // 2 + 1):
        for b in range(a, (n - a) // 2 + 1):
            if a != b and 2 * (a + b) == n:
                ways += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `ways` is the count of valid pairs \((a, b)\) such that \(a \neq b\) and \(2 \times (a + b) == n\).
    return ways
    #`The program returns the count of valid pairs (a, b) such that a ≠ b and 2 * (a + b) == n, where n is a positive integer`
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` such that \(1 \leq n \leq 2 \times 10^9\). It iterates through possible values of `a` and `b` to find pairs that satisfy the condition \(2 \times (a + b) == n\) and \(a \neq b\). For each valid pair found, it increments the counter `ways`. After executing the nested loops, the function returns the total count of such valid pairs. The function handles edge cases where no valid pairs exist by returning `0`.

