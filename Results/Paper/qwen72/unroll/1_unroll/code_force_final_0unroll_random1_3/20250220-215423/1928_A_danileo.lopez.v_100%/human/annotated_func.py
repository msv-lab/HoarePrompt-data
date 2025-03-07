#State of the program right berfore the function call: The function should take two parameters, a and b, which are integers such that 1 <= a, b <= 10^9, representing the dimensions of the rectangle. The function should also handle multiple test cases, where the number of test cases, t, is an integer such that 1 <= t <= 10^4.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            if a % 2 == 0:
                a1, a2 = a // 2, a // 2
                if a1 != b:
                    print('Yes')
                    continue
            if b % 2 == 0:
                b1, b2 = b // 2, b // 2
                if b1 != a:
                    print('Yes')
                    continue
            print('No')
        else:
            print('No')
        
    #State: The loop iterates `t` times, and for each iteration, it reads two integers `a` and `b` from the input. If either `a` or `b` is even, it checks if the even dimension can be split into two equal parts that are not equal to the other dimension. If this condition is met, it prints 'Yes'; otherwise, it prints 'No'. If both `a` and `b` are odd, it directly prints 'No'. After all iterations, the values of `t`, `a`, and `b` remain unchanged, but the loop has completed its execution and the corresponding output has been printed for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases (1 <= t <= 10^4). For each test case, it reads two integers `a` and `b` (1 <= a, b <= 10^9) representing the dimensions of a rectangle. The function checks if either dimension `a` or `b` is even and can be split into two equal parts that are not equal to the other dimension. If this condition is met, it prints 'Yes'; otherwise, it prints 'No'. If both dimensions are odd, it directly prints 'No'. After processing all test cases, the function does not return any value but prints the result for each test case. The values of `t`, `a`, and `b` remain unchanged after the function execution.

