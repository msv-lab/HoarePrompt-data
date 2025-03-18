#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, n and m are positive integers such that 1 <= n, m <= 2 * 10^6. The sum of n and the sum of m over all test cases do not exceed 2 * 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: `t` is a positive integer such that 1 <= t <= 10^4; `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6; `ans` is equal to `n` plus the sum of `(n + i) // (i * i)` for all `i` from `2` to `root`; `root` is `int(math.sqrt(n)) + 1`.
    print(ans)
    #This is printed: ans (where ans is n plus the sum of (n + i) // (i * i) for all i from 2 to root, and root is int(math.sqrt(n)) + 1)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `k` from the input, calculates a value `ans` based on `n`, and prints this value. The calculation involves summing up `n` plus the integer division of `(n + i)` by `(i * i)` for all `i` from `2` to the integer square root of `n` plus one. The function does not accept any parameters and does not return any value; it directly prints the result.

