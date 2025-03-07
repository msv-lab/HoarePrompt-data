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
        
    #State: Output State: `t` input integers between 1 and 50, inclusive; for each integer `n`, if `n` is odd, the output is 'NO'; if `n` is even and the length of 'AAB' * (n // 2) is less than 200, the output is 'YES' followed by the string 'AAB' * (n // 2); otherwise, the output is 'NO'.
#Overall this is what the function does:The function processes a series of integer inputs `t` and `n`. For each `n`, if `n` is odd, it outputs 'NO'. If `n` is even and the generated string 'AAB' repeated `(n // 2)` times is less than 200 characters long, it outputs 'YES' followed by the string. Otherwise, it outputs 'NO'. The function does not accept any parameters and does not return anything.

