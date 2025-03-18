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
        
    #State: Output State: The output state will consist of a series of lines, each containing either 'Draw', 'Alice', or 'Bob'. The number of lines will be equal to the number of test cases provided. For each test case, the output depends on the relative positions of the points (xa, ya) and (xb, yb) within the grid defined by dimensions h and w. If xa is greater than xb, the output is 'Draw'. Otherwise, it checks the vertical positions and determines if Alice or Bob wins based on their positions relative to the midpoint between xa and xb.
#Overall this is what the function does:The function processes multiple test cases, each consisting of grid dimensions \(h\) and \(w\), and two points \((x_a, y_a)\) and \((x_b, y_b)\). For each test case, it determines the winner based on the relative positions of these points within the grid. If \(x_a\) is greater than \(x_b\), it outputs 'Draw'. Otherwise, it calculates the midpoint between \(x_a\) and \(x_b\) and checks the vertical positions of \((x_a, y_a)\) and \((x_b, y_b)\) to decide between 'Alice' and 'Bob'. The function outputs a series of lines, each containing 'Draw', 'Alice', or 'Bob', corresponding to the outcome of each test case.

