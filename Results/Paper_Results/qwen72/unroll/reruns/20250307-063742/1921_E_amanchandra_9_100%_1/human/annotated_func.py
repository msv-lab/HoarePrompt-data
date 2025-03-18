#State of the program right berfore the function call: The function `func` is intended to process multiple test cases, each consisting of six integers: `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b`. The input is structured as follows: the first line contains an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, `h` and `w` are the dimensions of the board (1 ≤ h ≤ 10^6, 1 ≤ w ≤ 10^9), and `x_a`, `y_a`, `x_b`, `y_b` are the initial positions of Alice's and Bob's chips (1 ≤ x_a, x_b ≤ h, 1 ≤ y_a, y_b ≤ w) with the guarantee that the initial positions do not coincide (either x_a ≠ x_b or y_a ≠ y_b).
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
        
    #State: The loop will execute `t` times, and for each iteration, it will read six integers from the input and print either 'Draw', 'Alice', or 'Bob' based on the conditions in the loop. The values of `t`, `r`, `w`, `a`, `b`, `c`, and `d` will be consumed and not retained between iterations. After all iterations, the initial state of the variables outside the loop will remain unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each involving a game board with dimensions `h` and `w`, and initial positions of two chips, Alice's chip at `(x_a, y_a)` and Bob's chip at `(x_b, y_b)`. For each test case, it reads the input values, performs a series of calculations based on the positions of the chips, and prints either 'Draw', 'Alice', or 'Bob' depending on the conditions. The function does not return any value; instead, it directly outputs the result for each test case. After processing all test cases, the function consumes the input values and does not retain any state between iterations.

