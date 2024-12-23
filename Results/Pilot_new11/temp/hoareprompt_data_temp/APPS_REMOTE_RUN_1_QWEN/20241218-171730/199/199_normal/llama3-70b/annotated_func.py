#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2·10^9.
def func_1(n):
    ways = 0
    for a in range(1, n // 2 + 1):
        for b in range(a, (n - a) // 2 + 1):
            if a != b and 2 * (a + b) == n:
                ways += 1
        
    #State of the program after the  for loop has been executed: `ways` is the number of pairs (a, b) such that 1 ≤ a < b ≤ n//2 and 2 * (a + b) == n, `a` is the last value of `a` checked in the loop, `b` is the last value of `b` checked in the loop.
    return ways
    #`The program returns ways, which is the number of pairs (a, b) such that 1 ≤ a < b ≤ n//2 and 2 * (a + b) == n, and 'a' and 'b' are the last values of 'a' and 'b' checked in the loop, respectively`
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` (where \(1 \leq n \leq 2 \cdot 10^9\)) and returns the number of distinct pairs \((a, b)\) such that \(1 \leq a < b \leq \frac{n}{2}\) and \(2 \times (a + b) == n\). After the function execution, it also returns the last values of `a` and `b` that were checked in the loop. The function iterates over possible values of `a` and `b` to find valid pairs, incrementing the `ways` counter each time a valid pair is found.

