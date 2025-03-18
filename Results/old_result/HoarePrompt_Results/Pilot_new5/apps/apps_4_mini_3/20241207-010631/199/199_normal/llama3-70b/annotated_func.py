#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2·10^9.
def func_1(n):
    ways = 0
    for a in range(1, n // 2 + 1):
        for b in range(a, (n - a) // 2 + 1):
            if a != b and 2 * (a + b) == n:
                ways += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ n ≤ 2·10^9, `ways` is the total number of valid pairs (a, b) found such that 2 * (a + b) equals `n`, and `a` ranges from 1 to `n // 2`. If `n` is less than 2, then `ways` remains 0.
    return ways
    #The program returns the total number of valid pairs (a, b) such that 2 * (a + b) equals `n`, where `a` ranges from 1 to `n // 2`, and `ways` is 0 if `n` is less than 2.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the total number of distinct pairs (a, b) such that 2 * (a + b) equals `n`, with `a` ranging from 1 to `n // 2` and `b` ranging from `a` to `(n - a) // 2`. If `n` is less than 2, it returns 0. The function also ensures that `a` and `b` are not equal.

