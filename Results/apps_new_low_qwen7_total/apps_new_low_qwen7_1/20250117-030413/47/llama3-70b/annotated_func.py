#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 1 000 000.
def func():
    n, m = map(int, input().split())

count = 0
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if (x + y) % 5 == 0:
                count += 1
        
    #State of the program after the  for loop has been executed: `count` is the total number of integers `y` in the range from 1 to `m` such that `(x + y) % 5 == 0` for all `x` in the range from 1 to `n`. The value of `x` will have incremented to `n`, `n` and `m` remain the same as the initial values.
    print(count)
#Overall this is what the function does:The function reads two positive integers `n` and `m` from standard input, where \(1 \leq n, m \leq 1,000,000\). It then iterates over all pairs \((x, y)\) where \(1 \leq x \leq n\) and \(1 \leq y \leq m\), counting the number of pairs for which \((x + y) \% 5 == 0\). After completing the iteration, it prints the count of such pairs. The function does not accept any parameters and does not return a value. An edge case to consider is when either `n` or `m` is zero, in which case no valid pairs exist, and the count remains zero. There is no missing functionality in the provided code.

