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
        
    #State: `x` is the smallest integer greater than the square root of `n`, `cnt` is the sum of the minimum of `n / ((x + y) * x)` and `m // ((x + y) * y)` for all pairs `(x, y)` where `x * x <= n`, `(x + y) * x <= n`, `(x + y) * y <= m`, and `gcd(x, y) == 1`.
    print(cnt)
    #This is printed: cnt (where cnt is the sum of the minimum of `n / ((x + y) * x)` and `m // ((x + y) * y)` for all pairs `(x, y)` that satisfy `x * x <= n`, `(x + y) * x <= n`, `(x + y) * y <= m`, and `gcd(x, y) == 1`)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `m` from the user input, where `1 <= n, m <= 2 * 10^6`. It then calculates the number of pairs `(x, y)` such that `x * x <= n`, `(x + y) * x <= n`, `(x + y) * y <= m`, and `gcd(x, y) == 1`. The function prints this count as the final output. After the function concludes, the state of the program is that `x` is the smallest integer greater than the square root of `n`, and `cnt` holds the calculated count of valid pairs.

#State of the program right berfore the function call: None of the variables in the function signature are used, but the function assumes that `func_1` is defined and can handle the input and output as described in the problem.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The loop has executed `func_1` `t` times, but since `func_1` does not return any value or modify any variables in the loop head or body, the output state remains unchanged from the initial state.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, and then calls the function `func_1` exactly `t` times. The function does not return any value, and it does not modify any variables or state outside of its scope. The primary purpose of `func_2` is to execute `func_1` a specified number of times based on user input.

