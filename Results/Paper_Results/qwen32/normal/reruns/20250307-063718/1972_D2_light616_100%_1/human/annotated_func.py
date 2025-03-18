#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
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
        
    #State: x is 5, y is 4, cnt is at least 8.
    print(cnt)
    #This is printed: cnt (where cnt is at least 8)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `m` from the input, calculates a count based on certain conditions involving the greatest common divisor (GCD) of pairs of numbers, and prints this count.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 · 10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t is a specific positive integer input from the user and func_1() has been executed t times.
#Overall this is what the function does:The function `func_2` processes `t` test cases, where each test case consists of two positive integers `n` and `m` (1 ≤ n, m ≤ 2 · 10^6). For each test case, it calls `func_1()` which presumably performs some computation or evaluation based on `n` and `m`.

