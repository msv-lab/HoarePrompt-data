#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_1():
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n // ((x + y) * x), m // ((x + y) * y))
            y += 1
        
        x += 1
        
    #State: x is 7, y is 1, cnt is 19.
    print(cnt)
    #This is printed: 19
#Overall this is what the function does:The function `func_1` calculates and prints the count of pairs `(x, y)` where `x` and `y` are positive integers, `gcd(x, y) = 1`, and the product `(x + y) * x` does not exceed `n` and `(x + y) * y` does not exceed `m`.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 <= t <= 10^4. Each test case consists of two positive integers n and m, where 1 <= n, m <= 2 * 10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: the loop has executed `t` times, and `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` reads a positive integer `t` representing the number of test cases. For each test case, it calls `func_1`, which presumably processes two positive integers `n` and `m` provided as input. After processing all test cases, the function concludes without returning any explicit value.

