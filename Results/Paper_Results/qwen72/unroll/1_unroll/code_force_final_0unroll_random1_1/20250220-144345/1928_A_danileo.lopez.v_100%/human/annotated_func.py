#State of the program right berfore the function call: The function should accept two parameters, a and b, which are integers such that 1 <= a, b <= 10^9, representing the dimensions of the rectangle. The function should also be able to handle multiple test cases, where the number of test cases, t, is an integer such that 1 <= t <= 10^4.
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
        
    #State: The loop will have executed `t` times, where `t` is the number of test cases provided. For each test case, the values of `a` and `b` will be read from the input, and the loop will print 'Yes' if either `a` or `b` is even and the condition `a1 != b` or `b1 != a` is satisfied, otherwise it will print 'No'. The values of `a` and `b` will be overwritten in each iteration, and `t` will be decremented by 1 for each iteration until it reaches 0.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases (1 <= t <= 10^4). For each test case, it reads two integers `a` and `b` (1 <= a, b <= 10^9) from the input, representing the dimensions of a rectangle. The function checks if either `a` or `b` is even. If `a` is even and `a // 2` is not equal to `b`, or if `b` is even and `b // 2` is not equal to `a`, it prints 'Yes'. Otherwise, it prints 'No'. After processing all test cases, the function completes and the values of `a` and `b` are no longer relevant.

