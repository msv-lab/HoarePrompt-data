#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and n is an integer such that 1 <= n <= 50 for each test case.
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
        
    #State: `t` is an input integer such that 1 <= t <= 50, and `n` is an integer such that 1 <= n <= 50 for each test case. The loop has finished executing, and the values of `t` and `n` are unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 50`, and then for each of the `t` test cases, it reads another integer `n` (where `1 <= n <= 50`). For each `n`, if `n` is odd, it prints 'NO'. If `n` is even, it constructs a string `s` consisting of the pattern 'AAB' repeated `n // 2` times. If the length of `s` is less than 200, it prints 'YES' followed by the string `s`. Otherwise, it prints 'NO'. After processing all `t` test cases, the function concludes without returning any value. The values of `t` and `n` are not retained after the function execution.

