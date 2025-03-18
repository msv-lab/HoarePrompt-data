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
        
    #State: `t` is an integer such that `t` is 0; `n` is the input integer. If `n` is odd, the program does nothing further. If `n` is even, `s` is the string `'110'` repeated `n // 2` times, and `s` retains its initial value if its length is less than 200 or if its length is 200 or more.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n`. If `n` is odd, it outputs 'NO'. If `n` is even, it constructs a string `s` by repeating the substring '110' `n // 2` times and checks if the length of `s` is less than 200. If so, it outputs 'YES' followed by the string `s`; otherwise, it outputs 'NO'.

