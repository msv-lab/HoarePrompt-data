#State of the program right berfore the function call: The function `func` is expected to be called with no arguments, but the problem description indicates that the function should handle multiple test cases, each consisting of six integers: `h`, `w`, `x_a`, `y_a`, `x_b`, `y_b`. These integers should satisfy the conditions: 1 ≤ `x_a`, `x_b` ≤ `h` ≤ 10^6, 1 ≤ `y_a`, `y_b` ≤ `w` ≤ 10^9, and either `x_a` ≠ `x_b` or `y_a` ≠ `y_b`. The function should also handle the input of the number of test cases `t` (1 ≤ `t` ≤ 10^4). The sum of `h` over all test cases should not exceed 10^6.
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
        
    #State: The loop will execute `t` times, and for each iteration, it will read six integers from the input, perform the specified conditions, and print either 'Draw', 'Alice', or 'Bob' based on the conditions. After all iterations, the value of `t` will be unchanged, and the input variables for each test case (`r`, `w`, `a`, `b`, `c`, `d`) will be consumed and not retained. The output will be a series of strings, each either 'Draw', 'Alice', or 'Bob', corresponding to the result of each test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads six integers `r`, `w`, `a`, `b`, `c`, and `d` from the input. The function then determines and prints the result of a game for each test case, which can be either 'Draw', 'Alice', or 'Bob'. The result is based on the relative positions of `a` and `c`, and the distances between `b`, `d`, and the calculated values `l` and `r`. After processing all test cases, the function does not retain any of the input values, and the value of `t` remains unchanged. The final state of the program is that the input for each test case has been consumed, and the corresponding results have been printed.

