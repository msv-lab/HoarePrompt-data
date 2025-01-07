#State of the program right berfore the function call: n is a positive integer satisfying 1 ≤ n ≤ 2·10^9.
def func_1(n):
    ways = 0
    for a in range(1, n // 2 + 1):
        for b in range(a, (n - a) // 2 + 1):
            if a != b and 2 * (a + b) == n:
                ways += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer satisfying 1 ≤ n ≤ 2·10^9, `ways` is the count of unique pairs (a, b) such that `a + b = n / 2` and `a` is not equal to `b`, with `1 ≤ a < b` and `a` in the range from 1 to `n // 2`. If `n` is less than 2, `ways` remains 0, meaning no valid pairs exist.
    return ways
    #The program returns the count of unique pairs (a, b) such that a + b = n / 2, with the condition that a is not equal to b, 1 ≤ a < b, and 1 ≤ a ≤ n // 2, where ways remains 0 if n is less than 2.
#Overall this is what the function does:The function accepts a positive integer `n` and counts the number of unique pairs of integers `(a, b)` such that `a + b = n / 2`, where `a` is not equal to `b`, `1 ≤ a < b`, and `1 ≤ a ≤ n // 2`. If `n` is less than 2, the count of pairs remains 0. The pairs `(a, b)` are distinct in the sense that the order does not matter (i.e., `(a, b)` and `(b, a)` are considered the same). Notably, if `n` is odd or less than 2, the function will naturally return 0 since there can be no pairs satisfying the condition. Therefore, the function effectively performs a counting operation within defined constraints, resulting in a non-negative integer output.

