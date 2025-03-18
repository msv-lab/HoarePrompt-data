#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 1 <= n <= 50.
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
        
    #State: `t` is a specific integer such that 1 <= `t` <= 50; the loop has executed `t` times; for each of the `t` test cases, `n` is an input integer; if `n` is odd, the output is 'NO'; if `n` is even, then `s` is a string consisting of the substring `'110'` repeated `n // 2` times; if the length of `s` is less than 200, the output is 'YES' followed by `s`; otherwise, the output is 'NO'.
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer between 1 and 50. For each test case, it checks if the input integer `n` (where 1 <= n <= 50) is even. If `n` is odd, it outputs 'NO'. If `n` is even, it constructs a string `s` by repeating the substring '110' `n // 2` times. If the length of `s` is less than 200, it outputs 'YES' followed by the string `s`; otherwise, it outputs 'NO'.

