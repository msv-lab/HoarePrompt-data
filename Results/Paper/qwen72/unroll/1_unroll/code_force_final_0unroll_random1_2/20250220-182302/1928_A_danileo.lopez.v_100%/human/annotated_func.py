#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a and b are integers such that 1 <= a, b <= 10^9.
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
        
    #State: The loop has finished executing all iterations, and the values of `t`, `a`, and `b` remain unchanged. The loop prints 'Yes' or 'No' for each test case based on the conditions specified in the loop body.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by two integers `a` and `b` (1 <= a, b <= 10^9). It reads the number of test cases `t` (1 <= t <= 10^4) from user input. For each test case, it checks if either `a` or `b` is even. If `a` is even, it checks if `a // 2` is not equal to `b`, and if so, it prints 'Yes'. If `b` is even, it checks if `b // 2` is not equal to `a`, and if so, it prints 'Yes'. If neither condition is met, it prints 'No'. After processing all test cases, the function concludes without modifying the values of `t`, `a`, or `b`.

