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
        
    #State: `x` is 5, `y` is 1, `cnt` is 6.
    print(cnt)
    #This is printed: 6
#Overall this is what the function does:The function reads two positive integers `n` and `m` as input, then calculates and prints the count of pairs `(x, y)` where `x` and `y` are positive integers, `gcd(x, y) = 1`, and the conditions `(x + y) * x <= n` and `(x + y) * y <= m` are satisfied.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t is 0; result is t * (t + 1) // 2.
#Overall this is what the function does:The function `func_2` reads a positive integer `t` representing the number of test cases, then executes `func_1` for each test case. After processing all test cases, the function does not return any value explicitly, but the annotations suggest that the final state involves a calculation related to the sum of the first `t` natural numbers (`t * (t + 1) // 2`).

