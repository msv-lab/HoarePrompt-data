#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are non-negative integers satisfying 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
def func():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if (a + b + c) % 2 != 0:
            print(-1)
            continue
        
        x = (a + b + c) // 2
        
        y = a + b
        
        print(min(x, y))
        
    #State: Output State: `t` is an integer between 1 and 500 inclusive, `_` is the total number of iterations `t`, `a`, `b`, and `c` are integers entered by the user for each iteration, `x` is equal to half the sum of `a`, `b`, and `c` rounded down for each iteration where the sum is even, `y` is `a + b` for each iteration, and the sum of `a`, `b`, and `c` is even for each iteration where `min(x, y)` is printed.
    #
    #This means that after all iterations of the loop have finished, the variable `t` will hold the total number of iterations, `_` will be equal to `t`, and for each of the `t` iterations, the values of `a`, `b`, and `c` will be as they were input during those iterations. The variable `x` will contain the value of `(a + b + c) // 2` rounded down for each iteration where the sum of `a`, `b`, and `c` is even, and `y` will be `a + b` for each iteration. The loop ensures that the sum of `a`, `b`, and `c` is even before calculating `min(x, y)`, so `y` will always be used in the comparison when it is even.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, followed by `t` sets of three integers `a`, `b`, and `c` for each test case. It then checks if the sum of `a`, `b`, and `c` is even. If the sum is odd, it prints `-1` and continues to the next test case. For each valid set of `a`, `b`, and `c`, it calculates `x` as half the sum of `a`, `b`, and `c` rounded down, and `y` as `a + b`. It prints the minimum of `x` and `y`. After processing all test cases, the function does not return any value but prints the results for each test case.

