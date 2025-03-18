#State of the program right berfore the function call: The function `func` is expected to be called with no arguments, but the problem description indicates that it should handle multiple test cases, each consisting of six integers: h, w, x_a, y_a, x_b, y_b. These integers should satisfy the conditions 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b. The function should also handle an input integer t (1 ≤ t ≤ 10^4) representing the number of test cases.
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
        
    #State: The loop will execute `t` times, and for each test case, it will print either 'Draw', 'Alice', or 'Bob' based on the conditions provided in the loop. The values of `h`, `w`, `xa`, `ya`, `xb`, and `yb` will be read from input for each iteration, and the loop will continue to the next test case until all `t` test cases have been processed. The final state of the loop will be that all `t` test cases have been evaluated and the corresponding results printed.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by six integers: `h`, `w`, `x_a`, `y_a`, `x_b`, and `y_b`. It reads an integer `t` from input, which specifies the number of test cases. For each test case, it reads the six integers from input, evaluates certain conditions, and prints either 'Draw', 'Alice', or 'Bob' based on those conditions. After processing all `t` test cases, the function concludes with all results printed to the console. The function does not return any value.

