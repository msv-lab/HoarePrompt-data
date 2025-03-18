#State of the program right berfore the function call: The function `func` is incomplete and does not match the problem description. The correct function definition should include parameters for the board dimensions and the initial positions of Alice's and Bob's chips, such as `def func(t, h, w, x_a, y_a, x_b, y_b):`, where `t` is the number of test cases, `h` and `w` are the dimensions of the board, and `(x_a, y_a)` and `(x_b, y_b)` are the initial positions of Alice's and Bob's chips, respectively. Each of these parameters must satisfy the conditions: `1 <= t <= 10^4`, `1 <= h <= 10^6`, `1 <= w <= 10^9`, `1 <= x_a, x_b <= h`, `1 <= y_a, y_b <= w`, and either `x_a != x_b` or `y_a != y_b`.
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
        
    #State: After all iterations of the loop, the variables `t`, `h`, `w`, `x_a`, `y_a`, `x_b`, and `y_b` retain their initial values. The loop variable `_` will have been incremented `t` times, and the variables `r`, `w`, `a`, `b`, `c`, and `d` will have been reassigned `t` times, each time based on the input provided during that iteration. If `a > c` in any iteration, the program prints 'Draw' and retains the values of `r`, `w`, `a`, `b`, `c`, and `d` for that iteration. If `a <= c`, `x` is calculated as the integer division of the absolute difference between `a` and `c` by 2. If `abs(a - c)` is odd, `l` is set to the maximum of 1 and `d - x`, and `r` is set to the minimum of `w` and `d + x`. The program then prints 'Alice' if the conditions `abs(l - b) <= x + 1` and `abs(r - b) <= x + 1` are both true, otherwise it prints 'Draw'. If `abs(a - c)` is even, `l` is set to the maximum of 1 and `b - x`, and `r` is set to the minimum of `w` and `b + x`. The program then prints 'Bob' if the conditions `abs(l - d) <= x` and `abs(r - d) <= x` are both true, otherwise it prints 'Draw'.
#Overall this is what the function does:The function `func` reads input from the user to determine the number of test cases `t` and, for each test case, the dimensions of a board `r` and `w`, and the initial positions of two chips, Alice's chip at `(a, b)` and Bob's chip at `(c, d)`. The function then evaluates the positions of the chips and prints 'Draw', 'Alice', or 'Bob' based on the following rules: If Alice's chip's row `a` is greater than Bob's chip's row `c`, the function prints 'Draw'. If `a` is less than or equal to `c`, the function calculates `x` as the integer division of the absolute difference between `a` and `c` by 2. If this difference is odd, the function checks if Alice's chip can move to a position within a certain range of Bob's chip's column, and prints 'Alice' if it can, otherwise 'Draw'. If the difference is even, the function checks if Bob's chip can move to a position within a certain range of Alice's chip's column, and prints 'Bob' if it can, otherwise 'Draw'. After processing all test cases, the function concludes without returning any value.

