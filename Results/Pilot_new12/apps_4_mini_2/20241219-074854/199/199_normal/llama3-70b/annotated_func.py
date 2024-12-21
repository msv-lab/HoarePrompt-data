#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2·10^9.
def func_1(n):
    ways = 0
    for a in range(1, n // 2 + 1):
        for b in range(a, (n - a) // 2 + 1):
            if a != b and 2 * (a + b) == n:
                ways += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ n ≤ 2·10^9; `ways` is the count of unique pairs `(a, b)` where `a + b = n/2` and `a != b`; if `n` is odd or less than `2`, `ways` remains `0`.
    return ways
    #The program returns the count of unique pairs (a, b) where a + b = n/2 and a != b, which is stored in the variable 'ways'. If n is odd or less than 2, 'ways' remains 0.
#Overall this is what the function does:The function accepts a positive integer `n`, where 1 ≤ n ≤ 2·10^9. It calculates and returns the count of unique pairs of integers `(a, b)` such that `a + b` equals `n / 2` and `a` is not equal to `b`. If `n` is odd or less than 2, the function returns 0, since in those cases, no valid pairs can satisfy the condition. The function does not handle negative values or values of `n` greater than the specified limit, but its logic confines `n` to the stated range.

