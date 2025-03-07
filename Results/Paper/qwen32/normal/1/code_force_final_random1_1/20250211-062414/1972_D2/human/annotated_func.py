#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_1():
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n / ((x + y) * x), m // ((x + y) * y))
            y += 1
        
        x += 1
        
    #State: n = 100, m = 100, x = 11, y = 10, cnt = 27.
    print(cnt)
    #This is printed: 27
#Overall this is what the function does:The function reads two positive integers `n` and `m` from the input, then calculates and prints the count of certain pairs `(x, y)` where `x` and `y` are positive integers, `gcd(x, y) = 1`, and the conditions `(x + y) * x <= n` and `(x + y) * y <= m` are satisfied.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an input integer representing the number of test cases, where 1 <= `t` <= 10^4. The loop has executed `t` times, and no further changes to `t` or any other variables occur.
#Overall this is what the function does:The function `func_2` reads an integer `t` representing the number of test cases, then executes `func_1` exactly `t` times. No specific results are returned or modified; the focus is on processing each test case through `func_1`.

