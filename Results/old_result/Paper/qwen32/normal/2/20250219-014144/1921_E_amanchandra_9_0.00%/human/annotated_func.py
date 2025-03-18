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
        
    #State: The loop has executed `t` times, where `t` is the initial integer input. For each iteration, the program reads six integers `h`, `w`, `xa`, `ya`, `xb`, and `yb`. If `xa > xb`, it prints "Draw". Otherwise, it calculates `x` as `abs(xa - xb) // 2`. Depending on whether `abs(xa - xb)` is odd or even, it sets `l` and `r` accordingly and checks if certain conditions related to `ya` and `yb` are met to determine whether to print "Alice" or "Bob". After all iterations, no further changes are made to the variables, and the program ends.
#Overall this is what the function does:The function processes multiple test cases, each defined by the dimensions of a grid (`h` and `w`) and the coordinates of two distinct points (`(x_a, y_a)` and `(x_b, y_b)`). For each test case, it determines and prints the result of a game between Alice and Bob based on their positions relative to each other and the grid boundaries. The possible results are "Alice", "Bob", or "Draw".

