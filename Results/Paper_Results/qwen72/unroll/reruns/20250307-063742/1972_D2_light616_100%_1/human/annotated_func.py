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
        
    #State: `x` is the smallest integer greater than the square root of `n`, `cnt` is the sum of all valid pairs `(x, y)` where `x` and `y` are coprime and satisfy the conditions `(x + y) * x <= n` and `(x + y) * y <= m`.
    print(cnt)
    #This is printed: cnt (where cnt is the sum of all valid pairs (x, y) that are coprime and satisfy the conditions (x + y) * x <= n and (x + y) * y <= m)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `m` from the user input, where 1 <= n, m <= 2 * 10^6. It calculates the number of pairs (x, y) where x and y are coprime, and both (x + y) * x <= n and (x + y) * y <= m are satisfied. The function prints this count and does not return any value. After the function concludes, the program state includes the printed count of valid (x, y) pairs.

#State of the program right berfore the function call: None
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` remains the same as the input integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, and then calls the function `func_1` exactly `t` times. After the function concludes, the integer `t` remains unchanged, and the function itself does not return any value.

