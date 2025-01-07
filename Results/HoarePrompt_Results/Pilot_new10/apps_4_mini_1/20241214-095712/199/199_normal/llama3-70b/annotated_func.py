#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2·10^9.
def func_1(n):
    ways = 0
    for a in range(1, n // 2 + 1):
        for b in range(a, (n - a) // 2 + 1):
            if a != b and 2 * (a + b) == n:
                ways += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 2·10^9, `ways` is the number of distinct pairs `(a, b)` such that `2 * (a + b) = n` with `1 ≤ a < b` and `b` being within the specified range.
    return ways
    #The program returns the number of distinct pairs `(a, b)` such that `2 * (a + b) = n` with `1 ≤ a < b` and `b` being within the specified range
#Overall this is what the function does:The function accepts a positive integer `n` and returns the number of distinct pairs `(a, b)` such that `2 * (a + b) = n` with the constraints that `1 ≤ a < b` and both `a` and `b` must fit within the calculated bounds. The function does not handle cases where `n` is odd, which will result in zero pairs, as no two distinct integers would satisfy the equation in that scenario. Therefore, the function effectively counts the valid pairs only for even values of `n`.

