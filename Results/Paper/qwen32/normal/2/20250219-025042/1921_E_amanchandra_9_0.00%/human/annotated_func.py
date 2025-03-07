#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. The sum of h over all test cases does not exceed 10^6.
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
        
    #State: The loop has executed `t` times, where `t` is the initial integer input. For each iteration `i` from 0 to `t-1`, the program reads six integers `h`, `w`, `xa`, `ya`, `xb`, and `yb`. If `xa > xb`, it prints "Draw". Otherwise, it calculates `x = abs(xa - xb) // 2`. If `abs(xa - xb) % 2` is true (odd), it sets `l = max(1, yb - x)` and `r = min(w, yb + x)`. If `abs(l - ya) <= x + 1` and `abs(r - ya) <= x + 1`, it prints "Alice"; otherwise, it prints "Draw". If `abs(xa - xb) % 2` is false (even), it sets `l = max(1, ya - x)` and `r = min(w, yb + x)`. If `abs(l - yb) <= x` and `abs(r - yb) <= x`, it prints "Bob"; otherwise, it prints "Draw".
#Overall this is what the function does:The function processes multiple test cases, each consisting of grid dimensions and coordinates for two points. For each test case, it determines whether a player named Alice or Bob wins based on specific conditions related to the positions of the points, or if the game results in a draw.

