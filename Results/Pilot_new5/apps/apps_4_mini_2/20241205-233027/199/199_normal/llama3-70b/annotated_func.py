#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2·10^9.
def func_1(n):
    ways = 0
    for a in range(1, n // 2 + 1):
        for b in range(a, (n - a) // 2 + 1):
            if a != b and 2 * (a + b) == n:
                ways += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 2·10^9; `ways` is the count of valid pairs `(a, b)` such that `a + b = n / 2` with `a < b` and `a` and `b` are both positive integers. If no valid pairs exist, `ways` remains 0.
    return ways
    #The program returns the count of valid pairs (a, b) such that a + b = n / 2 with a < b, where 'ways' counts these valid pairs and remains 0 if no valid pairs exist.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the count of valid pairs `(a, b)` such that `a + b = n / 2` with `a < b`. It iterates over possible values of `a` and `b`, ensuring they are distinct and positive integers. If no valid pairs exist, the function returns 0. The function only works for values of `n` that are even since `n / 2` must be an integer for valid pairs to exist. If `n` is odd, it will always return 0, as there can be no valid pairs.

