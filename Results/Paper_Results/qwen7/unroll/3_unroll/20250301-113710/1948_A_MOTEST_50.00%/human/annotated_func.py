#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 1 ≤ n ≤ 50.
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
        
    #State: Output State: The screen is cleared, then for each iteration of the loop, depending on the value of `n`, either 'NO' is printed or 'YES' followed by a string `ans`. If `n` is even, `ans` consists of pairs of characters from 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' up to half the value of `n`. If `n` is odd, `ans` starts with 'AAA' followed by pairs of characters from 'C' to 'Z' up to `n-3`. After all iterations, the final state of the screen displays the results of each iteration.
#Overall this is what the function does:The function processes a series of test cases (up to 50) where for each case, it reads an integer `n` (between 1 and 50). Depending on whether `n` is even or odd, it prints 'YES' followed by a specific string `ans`. If `n` is even, `ans` consists of pairs of uppercase letters from 'A' to 'Z' up to half the value of `n`. If `n` is odd, `ans` starts with 'AAA' followed by pairs of letters from 'C' to 'Z' up to `n-3`. After processing all test cases, it clears the screen and outputs the results for each case.

