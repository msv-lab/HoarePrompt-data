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
        
    #State: All iterations of the loop have completed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` and then `t` integers `n`. If `n` is 1, it prints 'NO'. Otherwise, it constructs a string `ans` based on whether `n` is even or odd and prints 'YES' followed by the constructed string `ans`. The function does not return any value but prints output for each test case.

