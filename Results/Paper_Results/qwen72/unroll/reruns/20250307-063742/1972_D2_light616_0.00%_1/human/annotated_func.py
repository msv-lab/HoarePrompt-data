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
        
    #State: `x` is the smallest integer greater than the square root of `n`, `cnt` is the count of pairs (x, y) that satisfy the conditions within the loop.
    print(cnt)
    #This is printed: cnt (where cnt is the count of pairs (x, y) that satisfy the conditions within the loop)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `m` from the user input, where `1 <= n, m <= 2 * 10^6`. It then counts the number of pairs `(x, y)` such that `1 <= x <= sqrt(n)`, `1 <= y <= m`, and both `(x + y) * x <= n` and `(x + y) * y <= m` hold true, with the additional condition that the greatest common divisor (GCD) of `x` and `y` is 1. After counting, it prints the total count of such pairs. The function does not return any value.

#State of the program right berfore the function call: This function does not take any parameters, but it assumes that `func_1` is defined and can handle the input and output for each test case.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The value of `t` remains unchanged, and `func_1` is called `t` times.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user input, and then calls the predefined function `func_1` exactly `t` times. The value of `t` remains unchanged after the function concludes. The function itself does not return any value, but the overall postconditions are determined by the behavior of `func_1`.

