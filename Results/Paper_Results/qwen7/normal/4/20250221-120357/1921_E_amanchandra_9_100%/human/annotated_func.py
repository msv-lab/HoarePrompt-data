#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six integers h, w, x_a, y_a, x_b, y_b such that 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9. Additionally, it is guaranteed that either x_a ≠ x_b or y_a ≠ y_b, and the sum of h over all test cases does not exceed 10^6.
def func():
    t = int(input())
    for _ in range(t):
        r, w, a, b, c, d = list(map(int, input().split()))
        
        if a > c:
            print('Draw')
        else:
            x = abs(a - c) // 2
            if abs(a - c) % 2:
                l = max(1, d - x)
                r = min(w, d + x)
                print(*(['Draw'], ['Alice'])[abs(l - b) <= x + 1 and abs(r - b) <= 
                    x + 1])
            else:
                l = max(1, b - x)
                r = min(w, b + x)
                print(*(['Draw'], ['Bob'])[abs(l - d) <= x and abs(r - d) <= x])
        
    #State: After all iterations of the loop have finished, `t` will be 0, indicating that there are no more iterations left. The values of `r`, `w`, `a`, `b`, `c`, `d`, and `x` will be updated to the last set of values provided by the user input during the last iteration of the loop. `l` will also be updated to the maximum of 1 and either `d - x` or `b - x` depending on whether the absolute difference between `a` and `c` is odd or even.
#Overall this is what the function does:The function processes multiple test cases, each consisting of six integers \(h\), \(w\), \(x_a\), \(y_a\), \(x_b\), and \(y_b\). For each test case, it compares the positions \((x_a, y_a)\) and \((x_b, y_b)\) on a grid. If \(x_a\) is greater than \(x_b\), it prints 'Draw'. Otherwise, it calculates the midpoint between \(x_a\) and \(x_b\) and determines if either Alice or Bob wins based on their respective positions \(y_a\) and \(y_b\). The function outputs 'Alice' or 'Bob' if one of them wins, or 'Draw' otherwise. After processing all test cases, the function concludes with no parameters returned, only printing the results for each test case.

