#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 <= x_a, x_b <= h <= 10^6 and 1 <= y_a, y_b <= w <= 10^9. It is guaranteed that x_a != x_b or y_a != y_b, and the sum of h over all test cases does not exceed 10^6.
def func():
    for i in range(int(input())):
        h, w, xa, ya, xb, yb = map(int, input().split())
        
        if xa > xb:
            print('Draw')
        else:
            x = abs(xa - xb) // 2
            if abs(xa - xb) % 2:
                l = max(1, yb - x)
                r = min(w, yb + x)
                print(*(['Draw'], ['Alice'])[abs(l - ya) <= x + 1 and abs(r - ya) <=
                    x + 1])
            else:
                l = max(1, ya - x)
                r = min(w, yb + x)
                print(*(['Draw'], ['Bob'])[abs(l - yb) <= x and abs(r - yb) <= x])
        
    #State: t lines, each containing either "Alice", "Bob", or "Draw" based on the input values for each test case.
#Overall this is what the function does:The function processes `t` test cases, each defined by six integers `h`, `w`, `x_a`, `y_a`, `x_b`, and `y_b`. For each test case, it determines whether "Alice", "Bob", or "Draw" should be printed based on the relative positions of the points `(x_a, y_a)` and `(x_b, y_b)` within a grid of dimensions `h` by `w`. The function outputs a result for each test case.

