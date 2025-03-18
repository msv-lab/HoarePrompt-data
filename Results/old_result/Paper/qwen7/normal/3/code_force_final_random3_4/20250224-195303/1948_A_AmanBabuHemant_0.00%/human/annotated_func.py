#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 1 ≤ n ≤ 50.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = '110' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: After all iterations of the loop, `t` must be equal to the initial value of `t`, `n` is the integer input from the user for each iteration, and `s` is a string consisting of '110' repeated `n//2` times with a length of either less than 200 or exactly 200 for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` and `n`. For each test case, it checks if `n` is odd or even. If `n` is odd, it prints 'NO'. If `n` is even, it constructs a string `s` consisting of '110' repeated `n//2` times. If the length of `s` is less than 200, it prints 'YES' followed by `s`; otherwise, it prints 'NO'. After processing all test cases, the function does not return any value but prints the results for each test case.

