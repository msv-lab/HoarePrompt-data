#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif (a - b == -a, a) or (b - a == -b, b):
            print('no')
        elif (a - b) % 2 > 0 or (a - b) % 2 < 0:
            print('yes')
        else:
            print('no')
        
    #State: After all iterations of the loop, `t` is a positive integer such that \(1 \leq t \leq 10^4\). The variable `i` is equal to `t - 1`. For each iteration, `a` and `b` are updated to the positive integers provided by the input for that specific test case. The loop prints 'yes' if both `a` and `b` are even, or if the difference between `a` and `b` is odd. It prints 'no' if the conditions `(a - b == -a, a)` or `(b - a == -b, b)` are met, or if the difference between `a` and `b` is even.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `a` and `b`. The function then checks the following conditions for each pair of `a` and `b`: 
- If both `a` and `b` are even, it prints 'yes'.
- If the conditions `(a - b == -a, a)` or `(b - a == -b, b)` are met, it prints 'no'.
- If the difference between `a` and `b` is odd, it prints 'yes'.
- Otherwise, it prints 'no'. 
After processing all `t` test cases, the function completes without returning any value. The final state of the program is that `t` test cases have been processed, and the appropriate output ('yes' or 'no') has been printed for each test case.

