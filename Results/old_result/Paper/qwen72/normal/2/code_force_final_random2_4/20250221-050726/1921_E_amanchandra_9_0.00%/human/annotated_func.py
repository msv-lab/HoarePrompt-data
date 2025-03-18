#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. Each test case consists of six integers h, w, x_a, y_a, x_b, y_b where (1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9), representing the dimensions of the board and the initial positions of Alice's and Bob's chips. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b, ensuring the initial positions do not coincide.
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
        
    #State: `t` is a positive integer (1 ≤ t ≤ 10^4), `i` is `t-1`, `h` is the last input integer, `w` is the last input integer, `xa` is the last input integer, `ya` is the last input integer, `xb` is the last input integer, `yb` is the last input integer. If `xa > xb`, no changes are made to the variables. Otherwise, `x` is set to `(abs(xa - xb) // 2)`. If `abs(xa - xb)` is odd, `l` is set to `max(1, yb - x)` and `r` is set to `min(w, yb + x)`. If `abs(xa - xb)` is even, `l` is set to `max(1, ya - x)` and `r` is set to `min(w, yb + x)`.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by six integers: `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b`. For each test case, it determines the outcome of a game between two players, Alice and Bob, based on their chip positions on a board of dimensions `h` by `w`. The function prints "Draw" if Alice's chip is initially further down the board than Bob's. Otherwise, it calculates a value `x` and uses it to determine the possible winning positions for Alice or Bob. If certain conditions are met, it prints "Alice" or "Bob"; otherwise, it prints "Draw". After processing all test cases, the function ends, and the final state includes the last processed values of `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b`, and any intermediate variables used in the calculations.

