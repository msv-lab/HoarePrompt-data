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
        
    #State: For each test case, if n is odd, the output is 'NO'. If n is even and n // 2 * 3 < 200, the output is 'YES' followed by the string '110' repeated n // 2 times. Otherwise, if n is even and n // 2 * 3 ≥ 200, the output is 'NO'. The value of t and the values of n for each test case remain unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n`. If `n` is odd, it outputs 'NO'. If `n` is even and `n // 2 * 3` is less than 200, it outputs 'YES' followed by the string '110' repeated `n // 2` times. If `n` is even and `n // 2 * 3` is 200 or more, it outputs 'NO'. The values of `t` and `n` for each test case remain unchanged.

