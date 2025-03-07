#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, h and w are positive integers such that 1 <= h <= 10^6 and 1 <= w <= 10^9. x_a, y_a, x_b, and y_b are positive integers such that 1 <= x_a, x_b <= h and 1 <= y_a, y_b <= w. It is guaranteed that either x_a != x_b or y_a != y_b. The sum of h over all test cases does not exceed 10^6.
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
        
    #State: `t` is an input integer such that 1 <= t <= 10^4; `h` and `w` are positive integers such that 1 <= h <= 10^6 and 1 <= w <= 10^9; `x_a`, `y_a`, `x_b`, and `y_b` are positive integers such that 1 <= x_a, x_b <= h and 1 <= y_a, y_b <= w; It is guaranteed that either x_a != x_b or y_a != y_b. The sum of h over all test cases does not exceed 10^6.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of grid dimensions `h` and `w`, and coordinates of two distinct points `(a, b)` and `(c, d)` on the grid. For each test case, it determines and prints the result of a game where Alice and Bob compete based on their positions and the grid dimensions. The result can be 'Alice', 'Bob', or 'Draw'.

