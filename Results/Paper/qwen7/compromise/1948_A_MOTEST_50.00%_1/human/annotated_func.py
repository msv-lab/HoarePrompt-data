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
        
    #State: All iterations of the loop have completed. t is an input integer, and i is t. n is an integer such that 1 ≤ n ≤ 50. If n is 1, the loop prints 'NO'. Otherwise, ans is a string consisting of 'A' repeated 2 * (n // 2 - 1) times, followed by additional characters based on the value of n. Specifically, if n is odd, ans starts with 'AAA' followed by the pattern. x is n // 2 + 1, and j is less than n // 2 - 1.
#Overall this is what the function does:The function processes a series of test cases defined by the integer `t`. For each test case, it reads another integer `n`. If `n` is 1, it prints 'NO'. Otherwise, it constructs a string `ans` consisting of the letter 'A' repeated in a specific pattern based on the value of `n`. If `n` is even, `ans` contains pairs of letters 'A' up to `n//2` times. If `n` is odd, `ans` starts with 'AAA' followed by pairs of letters 'A' up to `n//2 - 1` times. After processing all test cases, the function prints 'YES' for each valid `n` and outputs the constructed string `ans`.

