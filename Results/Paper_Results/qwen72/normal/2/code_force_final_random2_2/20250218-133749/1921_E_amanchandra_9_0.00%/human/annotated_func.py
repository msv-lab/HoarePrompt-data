#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each of the t test cases consists of six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and (x_a, y_a) ≠ (x_b, y_b).
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
        
    #State: After the loop executes all iterations, `i` equals `t - 1`, and `t` remains unchanged. The values of `h`, `w`, `xa`, `ya`, `xb`, and `yb` are reset to new integers from the input for each iteration. For each iteration, if `xa` > `xb`, no changes are made to any variables. Otherwise, `x` is set to `(abs(xa - xb) // 2)`. If the absolute difference between `xa` and `xb` is odd, `l` is set to `max(1, yb - x)` and `r` is set to `min(w, yb + x)`. If the absolute difference is even, `l` is set to `max(1, ya - x)` and `r` is set to `min(w, yb + x)`.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by six integers: `h`, `w`, `xa`, `ya`, `xb`, and `yb`. These integers represent the dimensions of a grid (`h` by `w`) and two distinct points on the grid (`(xa, ya)` and `(xb, yb)`). For each test case, the function determines and prints a result based on the relative positions of these points. If `xa` is greater than `xb`, the function prints "Draw". Otherwise, it calculates a value `x` and uses it to determine a range `[l, r]` on the grid. Depending on the parity of the distance between `xa` and `xb`, and the positions of `ya` and `yb` within the calculated range, the function prints either "Alice", "Bob", or "Draw". After processing all test cases, the function completes without returning any value.

