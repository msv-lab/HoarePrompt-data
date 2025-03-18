#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 1 <= n <= 50.
def func():
    os.system('cls')
    s = string.ascii_uppercase
    t = int(input())
    for i in range(t):
        n = int(input())
        
        if n == 1:
            print('NO')
        else:
            ans = ''
            x = 0
            if n % 2 == 0:
                for j in range(n // 2):
                    ans += s[x] * 2
                    x += 1
            else:
                ans, x = 'AAA', 1
                for j in range(n // 2 - 1):
                    ans += s[x] * 2
                    x += 1
            print('YES')
            print(ans)
        
    #State: `t` is unchanged; `s` is `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`; `n`, `ans`, and `x` hold the values from the last test case processed.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n`. For each test case, it prints 'NO' if `n` is 1, and otherwise prints 'YES' followed by a string of length `n` composed of alternating uppercase letters. The string contains duplicate letters if `n` is even, and the first three characters are 'AAA' if `n` is odd, followed by alternating duplicate letters.

