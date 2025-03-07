#State of the program right berfore the function call: The function should take two parameters, a and b, which are integers such that 1 <= a, b <= 10^9, representing the dimensions of the rectangle. The function should also handle multiple test cases, where the number of test cases, t, is an integer such that 1 <= t <= 10^4.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is an input integer such that 1 <= `t` <= 10^4, `_` is a placeholder variable that has been incremented `t` times, and `a` and `b` are integers input by the user such that 1 <= `a`, `b` <= 10^9. The loop has executed `t` times, and for each iteration, the values of `a` and `b` were updated to new values provided by the user. If either `a` or `b` was even in any iteration, 'Yes' was printed; otherwise, 'No' was printed.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases (1 <= t <= 10^4). For each test case, it reads two integers `a` and `b` (1 <= a, b <= 10^9) from the input, representing the dimensions of a rectangle. The function then checks if either `a` or `b` is even. If at least one of them is even, it prints 'Yes'; otherwise, it prints 'No'. After processing all test cases, the function completes and does not return any value.

