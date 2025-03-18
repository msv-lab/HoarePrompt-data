#State of the program right berfore the function call: The function should be called with a single integer t (1 ≤ t ≤ 50) representing the number of test cases, and for each test case, a single integer n (1 ≤ n ≤ 50) is provided.
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
        
    #State: After all iterations, `t` is 0, `i` is `t - 1` (where `t` is the initial number of test cases), and `n` is an input integer for the last test case. If `n` is 1, no changes are made to `x`, `ans`, or `j`. If `n` is even and greater than 1, `x` is `n // 2`, `ans` is the string formed by concatenating each of the first `n // 2` characters of `s` repeated twice, and `j` is `n // 2 - 1`. If `n` is odd and greater than 1, `x` is `n // 2`, `ans` is 'AAA' + `s[1]` * 2 + `s[2]` * 2 + ... + `s[(n // 2 - 1)]` * 2, and `j` is `n // 2 - 2`.
#Overall this is what the function does:The function `func` does not return a list but instead processes a series of test cases. It accepts a single integer `t` (1 ≤ t ≤ 50) representing the number of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 50). If `n` is 1, it prints 'NO'. Otherwise, it prints 'YES' followed by a string `ans` constructed as follows: If `n` is even, `ans` is a string where each of the first `n // 2` uppercase letters from the alphabet is repeated twice. If `n` is odd, `ans` starts with 'AAA' and is followed by each of the next `n // 2 - 1` uppercase letters from the alphabet, each repeated twice. After processing all test cases, the function does not return any value.

