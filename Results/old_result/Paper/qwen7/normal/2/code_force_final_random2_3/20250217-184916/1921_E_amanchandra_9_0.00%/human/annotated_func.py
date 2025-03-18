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
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to the total number of test cases provided as input. For each iteration, the values of `h`, `w`, `xa`, `xb`, `ya`, and `yb` will be updated based on the input for that specific test case. The variables `l` and `r` will retain their final values determined during the last iteration of the loop for each respective test case. If `xa > xb`, the output for that test case will always be 'Draw'. Otherwise, the output will be 'Alice' if both conditions `abs(l - ya) <= x + 1` and `abs(r - ya) <= x + 1` are met, or 'Bob' if the conditions `abs(l - yb) <= x` and `abs(r - yb) <= x` are met. All other variables outside the loop, such as `t`, will remain unchanged from their initial state.
    #
    #In summary, the output state will include the total number of iterations (`i`), the final values of `h`, `w`, `xa`, `xb`, `ya`, and `yb` for each test case, and the corresponding outputs ('Draw', 'Alice', or 'Bob') for each test case, with `l` and `r` holding their last computed values within each test case's context.
#Overall this is what the function does:The function processes a series of test cases, each consisting of six integers \(h\), \(w\), \(x_a\), \(y_a\), \(x_b\), and \(y_b\). For each test case, it determines whether Alice or Bob wins based on the positions \(x_a\) and \(x_b\) and the ranges defined by \(y_a\) and \(y_b\). If \(x_a > x_b\), the function prints 'Draw'. Otherwise, it checks specific conditions to decide between 'Alice' or 'Bob'. The function outputs the results for each test case and the total number of test cases processed.

