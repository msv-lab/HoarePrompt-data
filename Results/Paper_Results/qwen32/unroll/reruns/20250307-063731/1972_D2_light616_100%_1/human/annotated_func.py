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
        
    #State: `n` remains `n`, `m` remains `m`, `x` is the smallest integer such that `x * x > n`, `cnt` is the total count of valid `(x, y)` pairs.
    print(cnt)
    #This is printed: cnt (where cnt is the total count of valid (x, y) pairs such that x is the smallest integer greater than the square root of n and the pairs satisfy some condition relative to n and m)
#Overall this is what the function does:The function `func_1` accepts two positive integer parameters `n` and `m` (where 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6). It calculates and prints the total count of valid `(x, y)` pairs such that the greatest common divisor (GCD) of `x` and `y` is 1, and the pairs satisfy the conditions `(x + y) * x <= n` and `(x + y) * y <= m`. The function does not return any value; it only prints the count.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` remains the input integer, and the loop variable `_` is no longer in scope.
#Overall this is what the function does:The function `func_2` processes `t` test cases, where for each test case, it performs some computation or comparison involving two positive integers `n` and `m` such that 1 <= n, m <= 2 * 10^6.

