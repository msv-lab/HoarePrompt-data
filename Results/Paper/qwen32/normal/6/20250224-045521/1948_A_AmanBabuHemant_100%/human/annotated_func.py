#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 1 <= n <= 50.
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
        
    #State: After all iterations, `t` is 0 and no further test cases are processed. For each of the initial `t` test cases, the output is either 'NO' if `n` is odd, or 'YES' followed by the string `s` (which is 'AAB' repeated `n // 2` times) if `n` is even and the length of `s` is less than 200. If the length of `s` is 200 or more, the output is 'NO'.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n`. For each test case, it checks if `n` is odd, in which case it outputs 'NO'. If `n` is even, it generates a string `s` by repeating 'AAB' `n // 2` times and outputs 'YES' followed by the string `s` if the length of `s` is less than 200. If the length of `s` is 200 or more, it outputs 'NO'.

