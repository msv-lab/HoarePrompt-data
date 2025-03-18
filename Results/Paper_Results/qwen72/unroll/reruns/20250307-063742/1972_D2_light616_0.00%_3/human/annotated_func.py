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
        
    #State: `x` is the smallest integer greater than `sqrt(n)`, `cnt` is the count of coprime pairs `(x, y)` such that `(x + y) * x <= n` and `(x + y) * y <= m`.
    print(cnt)
    #This is printed: - The `print(cnt)` statement will print the value of `cnt`, which is the count of valid coprime pairs `(x, y)`.
    #
    #Since the exact values of `n` and `m` are not provided, we cannot compute the exact numerical value of `cnt`. However, based on the given conditions, the print statement will output the count of valid coprime pairs `(x, y)` that satisfy the specified constraints.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `m` from the user input, where `1 <= n, m <= 2 * 10^6`. It then calculates and prints the count of coprime pairs `(x, y)` such that `(x + y) * x <= n` and `(x + y) * y <= m`. The function does not return any value; it only prints the result. After the function concludes, `x` is the smallest integer greater than `sqrt(n)`, and `cnt` holds the count of valid coprime pairs `(x, y)` that satisfy the given conditions.

#State of the program right berfore the function call: No variables are passed to the function `func_2`.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: No variables are passed to the function `func_2`, `t` is an input integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, and then calls the function `func_1` `t` times. After the function concludes, the program state includes the integer `t` and the effects of calling `func_1` `t` times, but no value is returned from `func_2`.

