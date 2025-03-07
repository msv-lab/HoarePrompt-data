#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six integers h, w, x_a, y_a, x_b, y_b such that 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. Additionally, it is guaranteed that either x_a ≠ x_b or y_a ≠ y_b, and the sum of h over all test cases does not exceed 10^6.
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
        
    #State: Output State: The output state will consist of a series of 'Draw', 'Alice', and 'Bob' based on the conditions specified within the loop for each test case. For each test case, if `xa > xb`, the output will be 'Draw'. Otherwise, depending on the positions of `ya` and `yb` relative to the calculated range, the output will be either 'Alice' or 'Bob'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of six integers (h, w, x_a, y_a, x_b, y_b). It checks if x_a and x_b are distinct and if y_a and y_b are distinct. Depending on the positions of (x_a, y_a) and (x_b, y_b), it outputs 'Draw', 'Alice', or 'Bob'. If x_a > x_b, it always outputs 'Draw'. Otherwise, it calculates a range based on the distance between x_a and x_b and checks if y_a or y_b falls within this range to determine the output.

