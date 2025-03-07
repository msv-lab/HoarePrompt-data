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
        
    #State: `n` and `m` remain as the input integers, `x` is the smallest integer such that `x * x > n`, `y` is 1, and `cnt` is the total count of valid pairs `(x, y)` where `gcd(x, y) == 1` and the conditions `(x + y) * x <= n` and `(x + y) * y <= m` are satisfied.
    print(cnt)
    #This is printed: - The `print(cnt)` statement will print the total count of valid pairs `(x, y)` that satisfy the given conditions.
    #
    #Since the exact values of `n` and `m` are not provided, we cannot compute the exact numerical value of `cnt`. However, based on the structure of the problem, the print statement will output the count of valid pairs `(x, y)`.
    #
    #Output:
#Overall this is what the function does:The function reads two positive integers `n` and `m` from the user input, where 1 <= n, m <= 2 * 10^6. It then calculates the number of valid pairs `(x, y)` such that `gcd(x, y) == 1` and both `(x + y) * x <= n` and `(x + y) * y <= m` are satisfied. After the calculation, it prints the total count of these valid pairs. The function does not return any value.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an input integer within the range 1 <= t <= 10^4, and `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the user input, where `1 <= t <= 10^4`. It then calls the function `func_1` exactly `t` times. The function does not return any value. After the function concludes, `t` remains the same integer that was input by the user, and `func_1` has been executed `t` times.

