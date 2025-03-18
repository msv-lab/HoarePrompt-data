#State of the program right berfore the function call: The function should be called with a single integer t (1 ≤ t ≤ 50) representing the number of test cases, and for each test case, a single integer n (1 ≤ n ≤ 50) representing the number of special characters required in the string.
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
        
    #State: After the loop executes all the iterations, `t` is greater than or equal to the number of iterations, `i` is `t - 1`, and for each iteration, `n` is an input integer. If `n` is 1, no changes are made to `x`, `j`, or `ans` for that iteration. If `n` is even, `ans` for that iteration is a string containing each character of `s` from index 0 to `n // 2 - 1` repeated twice, and `x` is set to `n // 2`, `j` is set to `n // 2 - 1`. If `n` is odd and at least 5, `ans` for that iteration is 'AAA' + each character of `s` from index 1 to `n // 2 - 1` repeated twice, and `x` is set to `n // 2`, `j` is set to `n // 2 - 2`.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It processes a series of test cases, where each test case involves an integer `n` (1 ≤ n ≤ 50) representing the number of special characters required in a string. For each test case, if `n` is 1, it prints 'NO'. Otherwise, it prints 'YES' followed by a string `ans` that is constructed as follows: If `n` is even, `ans` is a string where each character from the uppercase alphabet is repeated twice, up to `n // 2` characters. If `n` is odd and at least 3, `ans` starts with 'AAA' and is followed by each character from the uppercase alphabet (starting from the second character) repeated twice, up to `n // 2 - 1` additional characters. After processing all test cases, the function concludes with no further changes to the program state.

