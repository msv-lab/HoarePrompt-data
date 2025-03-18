#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 50, and for each test case, n is a positive integer such that 1 ≤ n ≤ 50.
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
        
    #State: After the loop executes all iterations, `t` will be 0, `n` will be an input integer such that 1 ≤ n ≤ 50, and `s` will be 'AAB' repeated `n // 2` times if `n` is even and the resulting string length is less than 200. Otherwise, `s` will not be defined or will be 'NO' printed.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads an integer `n`. If `n` is odd, it prints 'NO'. If `n` is even and the string 'AAB' repeated `n // 2` times is less than 200 characters, it prints 'YES' followed by the generated string; otherwise, it prints 'NO'. The function does not accept any parameters and does not return anything.

