#State of the program right berfore the function call: The function `func` is expected to be called with no arguments, but the problem description suggests that the function should handle multiple test cases, each consisting of six integers: h, w, x_a, y_a, x_b, y_b. The function should be modified to accept these parameters, and the precondition for these parameters is: h and w are positive integers representing the dimensions of the board (1 ≤ h ≤ 10^6, 1 ≤ w ≤ 10^9), x_a, y_a, x_b, y_b are positive integers representing the initial positions of Alice's and Bob's chips (1 ≤ x_a, x_b ≤ h, 1 ≤ y_a, y_b ≤ w), and it is guaranteed that the initial positions do not coincide (x_a ≠ x_b or y_a ≠ y_b). Additionally, the function should be able to handle up to 10^4 test cases.
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
        
    #State: The loop executes `t` times, and for each iteration, it reads a new set of inputs (r, w, a, b, c, d) and prints either 'Draw', 'Alice', or 'Bob' based on the conditions specified in the loop. The values of `t`, `h`, `w`, `x_a`, `y_a`, `x_b`, and `y_b` remain unchanged.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of six integers: `r`, `w`, `a`, `b`, `c`, `d`, representing the dimensions of a board and the initial positions of two chips. The function determines the winner of a game based on the positions of the chips and prints either 'Draw', 'Alice', or 'Bob' for each test case. The function does not return any value; it only prints the result for each test case. After the function concludes, the input values and the state of the program remain unchanged.

