#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2·10^9.
def func_1(n):
    ways = 0
    for a in range(1, n // 2 + 1):
        for b in range(a, (n - a) // 2 + 1):
            if a != b and 2 * (a + b) == n:
                ways += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ n ≤ 2·10^9, `ways` is the count of valid pairs (a, b) such that 2 * (a + b) = n, and `a` and `b` are integers within defined ranges with `a` not equal to `b`.
    return ways
    #The program returns the count of valid pairs (a, b) such that 2 * (a + b) = n, where a and b are integers within defined ranges and a is not equal to b.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the count of distinct pairs of integers `(a, b)` such that `a + b` equals `n / 2` and `a` is not equal to `b`. If no such pairs exist, it returns 0. The function will only find pairs where both `a` and `b` are less than or equal to `n/2`, ensuring that the pairs are valid.

