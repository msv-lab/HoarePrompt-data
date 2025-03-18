#State of the program right berfore the function call: The function should take two parameters, n and m, which are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: `ans` is equal to the initial value of `n` plus the sum of `(n + i) // (i * i)` for all `i` in the range from 2 to `root` (inclusive). `n`, `k`, and `root` remain unchanged.
    print(ans)
    #This is printed: ans (where ans is the initial value of n plus the sum of (n + i) // (i * i) for all i in the range from 2 to root (inclusive))
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from user input, but only uses `n` for computation. It calculates a value `ans` which is the initial value of `n` plus the sum of `(n + i) // (i * i)` for all integers `i` in the range from 2 to the square root of `n` (inclusive, rounded up). The function then prints this calculated value `ans`. The function does not return any value. The state of the program after the function concludes is that `ans` is printed, and the variables `n`, `k`, and `root` are unchanged.

