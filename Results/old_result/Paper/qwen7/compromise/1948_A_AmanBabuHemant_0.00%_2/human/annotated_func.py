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
        
    #State: Output State: `t` is an input integer between 1 and 50, inclusive. For each iteration of the loop:
    #- If the input integer `n` is odd, it prints 'NO'.
    #- If `n` is even and less than 400, it prints 'YES' followed by a string `s` consisting of '110' repeated `n//2` times, but only if the length of `s` is less than 200. Otherwise, it prints 'NO'.
#Overall this is what the function does:The function processes up to 50 test cases, each involving an integer `n`. For each `n`, it checks if `n` is odd or even. If `n` is odd, it outputs 'NO'. If `n` is even and the resulting string `s` (consisting of '110' repeated `n//2` times) is less than 200 characters, it outputs 'YES' followed by `s`; otherwise, it outputs 'NO'. The function does not return any value but prints the results for each test case.

