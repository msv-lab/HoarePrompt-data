#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 1 <= n <= 50.
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
        
    #State: t is an integer such that t is greater than or equal to 1; n is an input integer (from the last iteration); s is "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; i is equal to t; if n is 1, the program prints "NO". Otherwise, it prints "YES" and ans is set to the constructed string based on n (e.g., "AABBCC" if n is 6), and x is set to the corresponding value (e.g., 3 if n is 6).
#Overall this is what the function does:The function processes `t` test cases, where each test case involves an integer `n`. For each test case, if `n` is 1, it prints "NO". Otherwise, it prints "YES" followed by a constructed string of length `n` using uppercase letters from the alphabet, ensuring that the string is balanced with pairs of letters. If `n` is odd, the string starts with "AAA" followed by pairs of letters.

