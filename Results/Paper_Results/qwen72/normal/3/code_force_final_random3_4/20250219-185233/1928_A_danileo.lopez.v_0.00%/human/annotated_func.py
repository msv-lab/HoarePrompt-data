#State of the program right berfore the function call: Each test case consists of two integers a and b (1 ≤ a, b ≤ 10^9) representing the dimensions of Bob's rectangle. The function is expected to handle multiple test cases, where the number of test cases t is an integer (1 ≤ t ≤ 10^4).
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is an input integer (1 ≤ t ≤ 10^4), `_` is `t-1`, and `a` and `b` are integers provided by the user input. If `a` is even or `b` is even, the program does not modify `a` or `b`. Otherwise, if both `a` and `b` are odd, the program does not modify `a` or `b`.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b` representing the dimensions of a rectangle. The function prints 'Yes' if either `a` or `b` is even, and 'No' if both `a` and `b` are odd. The function does not return any value, and the final state of the program is that it has printed the results for all `t` test cases.

