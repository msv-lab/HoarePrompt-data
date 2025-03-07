#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each of the t test cases is described by six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6.
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
        
    #State: The loop has executed `t` times, where `t` is the initial input integer. For each test case, the program has determined and printed the result ('Alice', 'Bob', or 'Draw') based on the provided conditions. The variables `r`, `w`, `a`, `b`, `c`, and `d` are re-assigned for each iteration based on the input values of each test case, and no changes are made to these variables outside of the loop iterations.
#Overall this is what the function does:The function processes `t` test cases, each consisting of a rectangle defined by dimensions `h` and `w`, and two points within the rectangle defined by coordinates `(x_a, y_a)` and `(x_b, y_b)`. For each test case, it determines and prints the result ('Alice', 'Bob', or 'Draw') based on the relative positions of the points within the rectangle.

