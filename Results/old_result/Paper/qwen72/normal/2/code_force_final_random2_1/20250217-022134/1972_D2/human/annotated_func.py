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
        
    #State: `n` and `m` are positive integers provided by the input, `x` is the smallest integer such that `x * x > n`, `y` is 1, and `cnt` is the total count of valid pairs `(x, y)` that satisfy the conditions within the loop.
    print(cnt)
    #This is printed: m (where m is the second positive integer provided by the input)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `m` from the input, where 1 <= n, m <= 2 * 10^6. It then calculates the number of pairs (x, y) such that 1 <= x, y, (x + y) * x <= n, and (x + y) * y <= m, with the additional condition that the greatest common divisor (gcd) of x and y is 1. After performing this calculation, the function prints the count of such valid pairs. The final state of the program includes the printed count, and the original values of `n` and `m` remain unchanged.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` must be greater than or equal to 0, `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the user input, where `1 <= t <= 10^4`, and calls the function `func_1` exactly `t` times. After the function concludes, `t` remains unchanged, and `func_1` has been executed `t` times. The function does not return any value.

