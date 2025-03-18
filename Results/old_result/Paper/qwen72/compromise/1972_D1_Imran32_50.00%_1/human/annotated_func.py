#State of the program right berfore the function call: The function should take two positive integers n and m as inputs, where 1 <= n, m <= 2 * 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: `n` remains unchanged, `k` remains unchanged, `root` remains unchanged, `ans` is updated to `n + sum((n + i) // (i * i) for i in range(2, root + 1))`.
    print(ans)
    #This is printed: n + sum((n + i) // (i * i) for i in range(2, root + 1)) (where n is the value of n and root is the value of root)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `k` from the input, where `1 <= n, k <= 2 * 10^6`. It then calculates a value `ans` by adding `n` to the sum of `(n + i) // (i * i)` for each integer `i` from 2 to the square root of `n` (inclusive). The function prints the final value of `ans` and does not return any value. The variables `n` and `k` remain unchanged throughout the function's execution.

