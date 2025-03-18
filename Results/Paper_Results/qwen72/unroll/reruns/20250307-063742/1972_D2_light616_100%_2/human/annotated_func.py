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
        
    #State: `x` is the smallest integer greater than the square root of `n`, and `cnt` is the total count of pairs (x, y) where `x` and `y` are coprime, `x * x <= n`, and `(x + y) * x <= n` and `(x + y) * y <= m`.
    print(cnt)
    #This is printed: cnt (where cnt is the total count of pairs (x, y) that satisfy the given conditions: x and y are coprime, x * x <= n, (x + y) * x <= n, and (x + y) * y <= m)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `m` from the input, where `1 <= n, m <= 2 * 10^6`. It calculates the total count of pairs `(x, y)` where `x` and `y` are coprime, `x * x <= n`, and `(x + y) * x <= n` and `(x + y) * y <= m`. After the calculation, it prints the count `cnt` and does not return any value. The final state of the program is that `cnt` is printed, representing the total number of valid coprime pairs.

#State of the program right berfore the function call: t is a non-negative integer such that 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The value of `t` remains unchanged.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads a non-negative integer `t` from the user input, where 1 <= t <= 10^4, and then calls the function `func_1` exactly `t` times. The value of `t` remains unchanged after the function execution. The function does not return any value.

