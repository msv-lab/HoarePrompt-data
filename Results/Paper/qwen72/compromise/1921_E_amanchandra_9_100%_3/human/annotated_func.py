#State of the program right berfore the function call: The function `func` is intended to process game scenarios, but the function definition provided does not include any parameters. The correct function definition should include parameters for the board dimensions (h, w) and the initial positions of Alice's and Bob's chips (x_a, y_a, x_b, y_b). Each of these parameters should be integers, with h and w representing the height and width of the board, respectively, and (x_a, y_a) and (x_b, y_b) representing the initial positions of Alice's and Bob's chips, respectively. The conditions 1 ≤ x_a, x_b ≤ h ≤ 10^6 and 1 ≤ y_a, y_b ≤ w ≤ 10^9 must be satisfied, and it is guaranteed that either x_a ≠ x_b or y_a ≠ y_b.
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
        
    #State: The loop iterates `t` times, processing input scenarios for Alice's and Bob's chips on a board of dimensions (r, w) with initial positions (a, b) and (c, d). For each iteration, if `a` is greater than `c`, the output is 'Draw'. Otherwise, the loop calculates the positions and determines the winner based on the conditions provided. The variables `r`, `w`, `a`, `b`, `c`, and `d` are reset for each iteration, and the variable `t` is decremented by 1 for each iteration until it reaches 0. The initial values of `h`, `x_a`, `y_a`, `x_b`, and `y_b` remain unchanged.
#Overall this is what the function does:The function `func` processes multiple game scenarios. It reads an integer `t` from input, which specifies the number of scenarios to process. For each scenario, it reads six integers `r`, `w`, `a`, `b`, `c`, `d` from input, representing the height and width of the board, and the initial positions of Alice's and Bob's chips, respectively. The function then determines the outcome of the game for each scenario and prints either 'Draw' or the name of the winner ('Alice' or 'Bob') based on the positions of the chips. The function does not return any value; it only prints the results. After processing all scenarios, the function concludes, and the input variables `t`, `r`, `w`, `a`, `b`, `c`, and `d` are no longer relevant.

