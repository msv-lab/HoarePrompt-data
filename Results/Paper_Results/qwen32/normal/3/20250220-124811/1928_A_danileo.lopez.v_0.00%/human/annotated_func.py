#State of the program right berfore the function call: Each test case consists of two integers a and b (1 ≤ a, b ≤ 10^9) representing the dimensions of Bob's rectangle. There are t (1 ≤ t ≤ 10^4) such test cases.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: The loop has executed `t` times, where `t` is the number of test cases provided as input. For each test case, the program has read two integers `a` and `b`, and printed 'Yes' if at least one of `a` or `b` is even, or 'No' if both `a` and `b` are odd. The values of `t`, `a`, and `b` are not retained after the loop completes; only the outputs ('Yes' or 'No') for each test case are produced.
#Overall this is what the function does:The function reads multiple test cases, each consisting of two integers representing the dimensions of a rectangle. For each test case, it checks if at least one of the dimensions is even and prints 'Yes' if true, otherwise it prints 'No'. The function does not return any value; it only outputs 'Yes' or 'No' for each test case.

