#State of the program right berfore the function call: The function `func` is expected to be called with no arguments, but the problem description implies that it should be called with multiple test cases, each consisting of six integers: h, w, x_a, y_a, x_b, y_b. These integers must satisfy the conditions: 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b. Additionally, the sum of h over all test cases should not exceed 10^6.
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
        
    #State: The loop will execute the specified number of times, processing each set of six integers (h, w, xa, ya, xb, yb) and printing either "Draw", "Alice", or "Bob" based on the conditions provided. The variables `h`, `w`, `xa`, `ya`, `xb`, and `yb` will be updated with each iteration to reflect the next set of input values, but their final values will be the last set of inputs processed by the loop. The loop counter `i` will have the value equal to the number of test cases minus one after the loop finishes.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of six integers: `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b`. For each test case, it determines and prints one of three possible outcomes: "Draw", "Alice", or "Bob". The outcome is based on the relative positions of `x_a` and `x_b` and the distances between `y_a` and `y_b` within the bounds defined by `h` and `w`. After processing all test cases, the function completes, and the final state of the program includes the printed results for each test case. The function does not return any value.

