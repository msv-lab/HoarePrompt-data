#State of the program right berfore the function call: The function should handle a list of test cases, where each test case is a single integer n (1 ≤ n ≤ 50), and the function should generate a suitable string of uppercase Latin letters or report that no such string exists.
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
        
    #State: `s` is the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', `t` is the initial input integer, `i` is `t - 1`, and `n` is the last input integer. If `n` is 1, no changes are made to the variables. If `n` is greater than 1 and even, `x` is `n // 2`, `ans` is the string formed by concatenating the first `n // 2` characters of `s` each repeated twice, and `j` is `n // 2 - 1`. If `n` is greater than 1 and odd, `x` is `n // 2`, `ans` is 'AAABBCC...CC' (where 'C' is the last character added, and the total number of characters in `ans` is `3 + 2 * (n // 2 - 1)`), and `j` is `n // 2 - 2`.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by an integer `n` (1 ≤ n ≤ 50). For each test case, if `n` is 1, it prints 'NO'. If `n` is greater than 1, it prints 'YES' followed by a string of uppercase Latin letters. If `n` is even, the string consists of the first `n // 2` letters of the alphabet, each repeated twice. If `n` is odd, the string starts with 'AAA' and is followed by the next `n // 2 - 1` letters of the alphabet, each repeated twice. The function does not return any values; it only prints the results to the console.

