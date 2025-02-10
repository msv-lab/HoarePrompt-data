#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 1 ≤ n ≤ 50.
def func():
    os.system('cls')
    s = string.ascii_uppercase
    t = int(input())
    for i in range(t):
        n = int(input())
        
        if n % 2 == 1:
            print('NO')
        else:
            ans, x = '', 0
            x = 0
            for j in range(n // 2):
                ans += s[x] * 2
                x += 1
            print('YES')
            print(ans)
        
    #State: Postcondition: `t` must be at least 1, `i` equals the total number of iterations (which is `t`), `n` is an input integer converted to an integer, `x` is `n // 2`, and `ans` is a concatenated string where each character from `s` at index `x` is repeated twice for each iteration from 0 to `n // 2 - 1`. If `n` is odd, `x` remains as `n // 2`.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n`. For each `n`, if `n` is odd, it prints 'NO'. Otherwise, it constructs a string `ans` by repeating each character from a predefined uppercase alphabet string `s` twice for `n // 2` times and then prints 'YES' followed by the constructed string `ans`. The function iterates `t` times, where `t` is the total number of test cases provided by the user.

