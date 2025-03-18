#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six integers h, w, x_a, y_a, x_b, y_b such that 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b, and the sum of h over all test cases does not exceed 10^6.
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
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to the total number of test cases entered as input. For each iteration, the variables `h`, `w`, `xa`, `ya`, `xb`, and `yb` will hold the values obtained from the input for that specific test case. The variable `x` will be calculated based on the conditions within the loop body, either as `abs(xa - xb) // 2` or 0, depending on whether the absolute difference between `xa` and `xb` is even or odd. The variables `l` and `r` will also be updated according to the conditions specified in the loop body, ensuring they are within the valid ranges defined by the problem constraints.
    #
    #The final output of the program will consist of either 'Draw' or the name of the player ('Alice' or 'Bob') who wins the game, based on the calculations performed in each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of six integers (h, w, x_a, y_a, x_b, y_b). For each test case, it calculates the outcome based on the positions of points (x_a, y_a) and (x_b, y_b) on a grid of size h x w. If x_a is greater than x_b, it prints 'Draw'. Otherwise, it calculates the distance between x_a and x_b and determines if Alice or Bob wins based on the vertical distance and the calculated midpoint. The function returns 'Draw', 'Alice', or 'Bob' for each test case, indicating the winner or a draw.

