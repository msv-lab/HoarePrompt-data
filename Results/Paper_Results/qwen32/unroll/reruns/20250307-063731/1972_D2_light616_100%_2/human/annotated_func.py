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
        
    #State: the final value of `cnt` after all iterations.
    print(cnt)
    #This is printed: cnt (where cnt is the final value of cnt after all iterations)
#Overall this is what the function does:The function calculates and prints the count of pairs \((x, y)\) such that \(x \cdot y\) is coprime, and the product \((x + y) \cdot x\) does not exceed \(n\) and \((x + y) \cdot y\) does not exceed \(m\).

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t remains the same, and func_1() has been called t times.
#Overall this is what the function does:The function `func_2` reads a positive integer `t` representing the number of test cases, then calls `func_1` exactly `t` times to process each test case.

