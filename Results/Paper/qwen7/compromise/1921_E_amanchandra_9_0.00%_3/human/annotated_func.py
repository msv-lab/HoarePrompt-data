#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six positive integers h, w, x_a, y_a, x_b, y_b such that 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b, and the sum of h over all test cases does not exceed 10^6.
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
        
    #State: Output State: The output state will consist of a series of 'Draw', 'Alice', and 'Bob' based on the conditions specified within the loop for each test case. For each test case, if `xa > xb`, it prints 'Draw'. Otherwise, it calculates the value of `x` as half the absolute difference between `xa` and `xb`. Depending on whether this difference is odd or even, it then determines the range `[l, r]` and checks if the vertical position `ya` or `yb` falls within certain conditions to decide whether 'Alice' or 'Bob' wins. If neither condition is met, it prints 'Draw'.
#Overall this is what the function does:The function processes multiple test cases, each containing six integers representing dimensions and positions. For each test case, it compares two positions (xa, ya) and (xb, yb). If xa is greater than xb, it prints 'Draw'. Otherwise, it calculates the horizontal distance between xa and xb and uses this to determine if the vertical position ya or yb falls within a specific range. Depending on whether this distance is odd or even, it decides if 'Alice' or 'Bob' wins, or if the result is 'Draw' again. The function returns a series of 'Draw', 'Alice', and 'Bob' based on these conditions for each test case.

