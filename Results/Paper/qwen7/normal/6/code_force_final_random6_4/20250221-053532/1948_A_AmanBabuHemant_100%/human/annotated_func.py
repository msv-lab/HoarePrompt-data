#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 1 ≤ n ≤ 50.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = 'AAB' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: After all iterations of the loop have finished, `t` will be 0, and there will be no further inputs or outputs from the loop.
#Overall this is what the function does:The function reads an integer `t` and then processes `t` test cases. For each test case, it reads an integer `n`, checks if `n` is even, and either prints 'NO' or constructs a string `s` consisting of 'AAB' repeated `(n // 2)` times. If the length of `s` is less than 200, it prints 'YES' followed by `s`; otherwise, it prints 'NO'. After processing all test cases, the function does not return any value.

