#State of the program right berfore the function call: The function should take an integer t (1 ≤ t ≤ 50) representing the number of test cases, and for each test case, an integer n (1 ≤ n ≤ 50) representing the number of special characters required in the string.
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
        
    #State: `t` is 0, `i` is `t` (the number of iterations completed), `n` is an input integer, and `s` is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. If `n` is 1, no changes are made to the variables and `ans` remains an empty string. If `n` is even, `ans` is the first `n // 2` characters of `s` each repeated twice, and `x` is `n // 2`, `j` is `n // 2 - 1`. If `n` is odd and greater than or equal to 7, `ans` is 'AAA' + the characters from `s[1]` to `s[(n // 2 - 1)]` each repeated twice, and `x` is `(n // 2 - 1) + 1`, `j` is `(n // 2 - 2)`. If `n` is odd and less than 7, `ans` is 'AAA' + the characters from `s[1]` to `s[(n // 2 - 1)]` each repeated twice, and `x` is `n // 2`, `j` is `n // 2 - 2`.
#Overall this is what the function does:The function `func` takes no parameters and does not return any value. It reads an integer `t` from the user, representing the number of test cases, and for each test case, it reads another integer `n`. If `n` is 1, it prints 'NO'. Otherwise, it prints 'YES' followed by a string `ans` that contains exactly `n` uppercase letters. If `n` is even, `ans` consists of the first `n // 2` letters of the alphabet, each repeated twice. If `n` is odd and greater than 1, `ans` starts with 'AAA' and is followed by the next `n // 2 - 1` letters of the alphabet, each repeated twice. After processing all test cases, the function concludes.

