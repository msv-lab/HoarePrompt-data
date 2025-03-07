#State of the program right berfore the function call: Each test case consists of six integers h, w, x_a, y_a, x_b, y_b where 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b. The number of test cases t satisfies 1 ≤ t ≤ 10^4, and the sum of h over all test cases does not exceed 10^6.
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
        
    #State: The output state consists of a series of strings printed for each test case, indicating either 'Alice', 'Bob', or 'Draw' based on the given conditions. The values of h, w, xa, ya, xb, yb remain unchanged from the initial state for each test case, and the number of test cases t also remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each involving a grid of dimensions `h` by `w` and two distinct points `(x_a, y_a)` and `(x_b, y_b)` on this grid. For each test case, it prints 'Alice', 'Bob', or 'Draw' based on the relative positions of these points. The input values remain unchanged after processing each test case.

