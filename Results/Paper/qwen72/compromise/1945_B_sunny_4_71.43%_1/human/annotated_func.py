#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are positive integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: The loop executes t times, and for each iteration, it reads three integers a, b, and m from the input, calculates A and B as int(m / a) + 1 and int(m / b) + 1 respectively, and prints the sum A + B. After all iterations, the values of t, a, b, and m remain unchanged, but the values of A and B are not retained between iterations.
#Overall this is what the function does:The function `func` reads a positive integer `t` indicating the number of test cases. For each test case, it reads three positive integers `a`, `b`, and `m`, calculates `A` as `int(m / a) + 1` and `B` as `int(m / b) + 1`, and prints the sum `A + B`. The function does not return any value, and the values of `t`, `a`, `b`, and `m` are not retained after each test case. After all test cases are processed, the function concludes without modifying the input variables.

