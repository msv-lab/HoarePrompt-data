#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each of the t test cases, n is an integer such that 1 ≤ n ≤ 50.
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
        
    #State: The variable `t` remains unchanged, and the program will have printed 'NO', 'YES', or a string of '110's based on the values of `n` provided during each iteration of the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n`. If `n` is odd, it prints 'NO'. If `n` is even, it constructs a string `s` consisting of the repetition of '110' `n // 2` times. If the length of `s` is less than 200, it prints 'YES' followed by the string `s`; otherwise, it prints 'NO'.

