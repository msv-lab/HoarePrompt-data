#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and n is an integer such that 1 <= n <= 50 for each test case.
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
        
    #State: `t` is an input integer such that 1 <= t <= 50, `n` is an integer such that 1 <= n <= 50 for each test case, the console screen is cleared, `s` is the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. The loop has executed `t` times, and for each iteration, if `n` was 1, 'NO' was printed. If `n` was greater than 1, 'YES' was printed followed by a string `ans` constructed as follows: if `n` was even, `ans` contains each of the first `n // 2` letters of `s` repeated twice; if `n` was odd, `ans` starts with 'AAA' and then contains each of the next `n // 2 - 1` letters of `s` repeated twice.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It clears the console screen and then reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads another integer `n` from the user. If `n` is 1, it prints 'NO'. If `n` is greater than 1, it prints 'YES' followed by a string `ans`. The string `ans` is constructed such that if `n` is even, it contains each of the first `n // 2` letters of the uppercase English alphabet repeated twice. If `n` is odd, `ans` starts with 'AAA' and then contains each of the next `n // 2 - 1` letters of the alphabet repeated twice. The function executes this process `t` times.

