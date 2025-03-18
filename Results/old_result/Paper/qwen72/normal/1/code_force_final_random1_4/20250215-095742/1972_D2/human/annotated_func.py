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
        
    #State: After all iterations of the loop, `n` and `m` remain positive integers such that \(1 \leq n, m \leq 2 \times 10^6\). The value of `x` is the smallest integer greater than 1 such that \(x \times x > n\). The value of `y` is 1. The value of `cnt` is the sum of `min(n / ((x + y) * x), m // ((x + y) * y))` for all pairs of `x` and `y` where `math.gcd(x, y) == 1` and the conditions \((x + y) * x <= n\) and \((x + y) * y <= m\) are satisfied.
    print(cnt)
    #This is printed: cnt (where cnt is the sum of min(n / ((x + y) * x), m // ((x + y) * y)) for all pairs of x and y where math.gcd(x, y) == 1 and (x + y) * x <= n and (x + y) * y <= m)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `m` from the user input, where both `n` and `m` are within the range 1 to 2 * 10^6. It then calculates the number of pairs `(x, y)` such that `x` and `y` are coprime (i.e., their greatest common divisor is 1), and the conditions \((x + y) * x <= n\) and \((x + y) * y <= m\) are satisfied. The function prints the count of such pairs. After the function completes, the values of `n` and `m` remain unchanged, and the function does not return any value.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an input integer such that 1 <= t <= 10^4, `_` is a placeholder (no specific value needed), and `func_1()` has been called `t` times, with 0 remaining iterations.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the user input, where `1 <= t <= 10^4`. It then calls the function `func_1` exactly `t` times. After the function completes, `t` remains the same integer value read from the input, and `func_1` has been executed `t` times. The function does not return any value.

