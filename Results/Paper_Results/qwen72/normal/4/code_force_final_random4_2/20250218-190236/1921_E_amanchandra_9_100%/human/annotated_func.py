#State of the program right berfore the function call: The function `func` is expected to be called within a context where the input is provided in the form of multiple test cases, each consisting of six integers: `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b`. The integers satisfy the conditions: 1 ≤ `x_a`, `x_b` ≤ `h` ≤ 10^6, 1 ≤ `y_a`, `y_b` ≤ `w` ≤ 10^9, and either `x_a` ≠ `x_b` or `y_a` ≠ `y_b`. The function should handle the input and output as described in the problem statement.
def func():
    t = int(input())
    for _ in range(t):
        r, w, a, b, c, d = list(map(int, input().split()))
        
        if a > c:
            print('Draw')
        else:
            x = abs(a - c) // 2
            if abs(a - c) % 2:
                l = max(1, d - x)
                r = min(w, d + x)
                print(*(['Draw'], ['Alice'])[abs(l - b) <= x + 1 and abs(r - b) <= 
                    x + 1])
            else:
                l = max(1, b - x)
                r = min(w, b + x)
                print(*(['Draw'], ['Bob'])[abs(l - d) <= x and abs(r - d) <= x])
        
    #State: `t` is 0, `_` is `t - 1`, `r`, `w`, `a`, `b`, `c`, and `d` are integers provided by the user. If `a` > `c`, the variables retain their initial values. If `a` ≤ `c`, `x` is the integer result of `abs(a - c) // 2`. If `abs(a - c) % 2` is true (i.e., `a - c` is odd), `l` is the maximum of 1 and `d - x`, and `r` is the minimum of `w` and `d + x`. Otherwise, `l` is the maximum of 1 and `b - x`, and `r` is the minimum of `w` and `b + x`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads six integers `r`, `w`, `a`, `b`, `c`, and `d` from the input. The function then determines and prints the outcome of a game based on the values of these integers. If `a` is greater than `c`, it prints 'Draw'. If `a` is less than or equal to `c`, it calculates `x` as the integer division of `abs(a - c)` by 2. Depending on whether `abs(a - c)` is odd or even, it further calculates `l` and `r` and prints either 'Draw', 'Alice', or 'Bob' based on specific conditions involving `l`, `r`, `b`, and `d`. After processing all test cases, the function concludes with the input variables `t`, `r`, `w`, `a`, `b`, `c`, and `d` being in their final states as determined by the input and the conditions within the function.

