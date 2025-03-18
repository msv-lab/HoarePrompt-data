#State of the program right berfore the function call: The function `func` is intended to process game scenarios but lacks parameters in its definition. For a correct implementation, it should accept parameters for the number of test cases `t`, the dimensions of the board `h` and `w`, and the initial positions of Alice's and Bob's chips `x_a`, `y_a`, `x_b`, `y_b`. Each of these parameters should satisfy the conditions: 1 ≤ t ≤ 10^4, 1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9, and either x_a ≠ x_b or y_a ≠ y_b.
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
        
    #State: The loop iterates `t` times, processing input for each test case and printing the result ('Draw', 'Alice', or 'Bob') based on the conditions specified. The values of `t`, `r`, `w`, `a`, `b`, `c`, and `d` are not retained between iterations, and the loop does not modify any variables outside its scope. Therefore, the initial state of the variables `t`, `h`, `w`, `x_a`, `y_a`, `x_b`, and `y_b` remains unchanged.
#Overall this is what the function does:The function `func` processes multiple game scenarios. It reads the number of test cases `t` from the input, and for each test case, it reads the dimensions of the board `r` and `w`, and the initial positions of Alice's and Bob's chips `a`, `b`, `c`, and `d`. The function then determines and prints the outcome ('Draw', 'Alice', or 'Bob') for each test case based on the positions of the chips. The function does not return any value; it only prints the results. The initial state of the variables `t`, `r`, `w`, `a`, `b`, `c`, and `d` is not retained between iterations, and no variables outside the function's scope are modified.

