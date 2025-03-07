#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 50, and for each test case, n is a positive integer such that 1 ≤ n ≤ 50.
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
        
    #State: All iterations of the loop have been executed, with `t` remaining greater than 0. The value of `n` provided in each iteration will determine the content of `ans`. If `n` is 1, `ans` will be the result of doubling the character at index 0 of `s` (which is 'A'). For even `n`, `ans` will be a string where every character from `s` (up to `n // 2 - 1`) is doubled. For odd `n`, `ans` will start with 'AAA' followed by the characters from `s` (from index 1 to `n // 2 - 1`) each doubled. The variable `x` will always be set to `n // 2` after the loop completes, and `j` will be `n // 2` or `n // 2 - 1` depending on whether `n` is even or odd.
#Overall this is what the function does:The function processes a series of test cases specified by `t`. For each test case, it reads an integer `n`. If `n` is 1, it prints 'NO'. Otherwise, it constructs a string `ans` based on the value of `n`. If `n` is even, `ans` consists of pairs of characters from the uppercase alphabet string `s`, up to `n // 2` characters. If `n` is odd, `ans` starts with 'AAA' followed by pairs of characters from `s`, up to `n // 2 - 1` characters. After processing all test cases, it prints 'YES' and the constructed string `ans` for each valid `n`.

