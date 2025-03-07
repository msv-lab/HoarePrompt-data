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
        
    #State: `t` is an integer such that `t` equals 0; no further changes are made to `t` or `n` after all iterations are complete. For each of the initial `t` test cases, if `n` is odd, the output is 'NO'. If `n` is even and the length of the string `s` (formed by repeating 'AAB' `n // 2` times) is less than 200, the output is 'YES' followed by the string `s`. If `n` is even and the length of `s` is 200 or more, the output is 'NO'.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of an integer `n`. For each test case, it checks if `n` is odd, in which case it outputs 'NO'. If `n` is even, it constructs a string `s` by repeating the substring 'AAB' `n // 2` times. If the length of `s` is less than 200, it outputs 'YES' followed by the string `s`; otherwise, it outputs 'NO'.

