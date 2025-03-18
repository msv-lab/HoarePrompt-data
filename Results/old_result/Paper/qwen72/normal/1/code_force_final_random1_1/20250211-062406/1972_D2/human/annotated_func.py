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
        
    #State: After all iterations, `n` and `m` are positive integers provided by the user, `x` is the smallest integer such that `x * x > n`, `y` is 1, and `cnt` is the total count of valid `(x, y)` pairs where `math.gcd(x, y) == 1` and `(x + y) * x <= n` and `(x + y) * y <= m`.
    print(cnt)
    #This is printed: The `print(cnt)` statement will print the total count of valid `(x, y)` pairs where `x` is the smallest integer such that `x * x > n`, `y` is 1, and the pairs satisfy the conditions `(x + 1) * x <= n` and `x + 1 <= m`.
    #
    #Output:
#Overall this is what the function does:The function reads two positive integers `n` and `m` from user input, where 1 <= n, m <= 2 * 10^6. It calculates and prints the total count of valid pairs `(x, y)` such that `1 <= x, y`, `gcd(x, y) == 1`, and both `(x + y) * x <= n` and `(x + y) * y <= m`. The function does not return any value; it only prints the result. After the function concludes, the program state includes the original values of `n` and `m`, and the printed count of valid `(x, y)` pairs.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` must be greater than or equal to 1, `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` reads an integer `t` from user input, where `1 <= t <= 10^4`. It then calls the function `func_1` exactly `t` times. After the function concludes, `func_1` has been executed `t` times, and the value of `t` remains unchanged. The function does not return any value.

