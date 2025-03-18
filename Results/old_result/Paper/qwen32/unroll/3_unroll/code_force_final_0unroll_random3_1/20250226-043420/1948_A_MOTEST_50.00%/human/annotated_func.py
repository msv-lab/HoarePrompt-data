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
        
    #State: t is an input integer, n is an integer such that 1 <= n <= 50, s is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n`. If `n` is 1, it prints 'NO'. Otherwise, it constructs a string of length `n` using uppercase letters from the alphabet, ensuring that the string is composed of pairs of the same letter, and prints 'YES' followed by the constructed string.

