#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of six positive integers h, w, x_a, y_a, x_b, y_b such that 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9, and it is guaranteed that either x_a ≠ x_b or y_a ≠ y_b. Additionally, the sum of h over all test cases does not exceed 10^6.
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
        
    #State: Output State: After the loop executes all its iterations, the values of `r`, `w`, `a`, `b`, `c`, `d`, `x`, and `l` will be updated according to the conditions inside the loop for each iteration. Specifically, `r` and `w` will be adjusted based on the comparison between `a` and `c`, and the values of `x`, `l`, `b`, and `d`. The variable `t` will be decremented with each iteration until it reaches 0. The final values of `r` and `w` will be the minimum of `w` and the adjusted values based on the conditions in the loop. The values of `a`, `b`, `c`, `d`, `x`, and `l` will reflect the last set of calculations performed within the loop for the final iteration. If `a > c`, the outcome will always be 'Draw'. Otherwise, the outcome will depend on the relative positions of `l`, `b`, and `r` compared to `d` and `x`.
    #
    #The exact final values of `r` and `w` cannot be determined without knowing the specific inputs for each iteration, but they will be the result of the loop's logic applied to each set of inputs.
#Overall this is what the function does:The function processes multiple test cases, each consisting of six positive integers \(h\), \(w\), \(x_a\), \(y_a\), \(x_b\), and \(y_b\). For each test case, it checks if \(x_a\) and \(x_b\) are different or \(y_a\) and \(y_b\) are different. If the conditions are met, it calculates whether Alice or Bob wins based on their positions. The function prints 'Draw' if \(a > c\), otherwise it determines the winner based on the relative positions of the calculated ranges. The function does not return any value but prints the outcome for each test case.

