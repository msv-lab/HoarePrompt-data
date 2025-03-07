#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each test case, n is an integer such that 1 <= n <= 50.
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
        
    #State: `t` is the initial input integer, `n` is the last input integer during the loop iterations, `s` is the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `i` is equal to `t`, and `ans` and `x` depend on the last value of `n` input.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n`. For each test case, it prints 'NO' if `n` is 1, otherwise it prints 'YES' and a string consisting of `n` uppercase letters where each letter appears twice consecutively, except when `n` is odd, in which case the first three letters are 'AAA' followed by pairs of letters.

