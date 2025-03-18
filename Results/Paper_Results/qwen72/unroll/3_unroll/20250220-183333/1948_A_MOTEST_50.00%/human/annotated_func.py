#State of the program right berfore the function call: The function should take an integer n as input, where 1 <= n <= 50, and return a string or a specific message based on the problem description.
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
        
    #State: The loop will execute `t` times, each time taking an integer `n` as input. For each iteration: If `n` is 1, it prints 'NO'. Otherwise, it prints 'YES' followed by a string `ans` constructed from the first `n // 2` characters of `s`, each repeated twice, starting from 'A'. If `n` is odd, the string starts with 'AAA' and then continues with the pattern. The variable `s` remains unchanged as 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. The variable `t` is decremented by 1 for each iteration until the loop completes.
#Overall this is what the function does:The function `func` does not return any value but performs the following actions: It first clears the console screen. It then reads an integer `t` from the user, representing the number of test cases. For each of the `t` test cases, it reads an integer `n` from the user. If `n` is 1, it prints 'NO'. Otherwise, it prints 'YES' followed by a string `ans`. The string `ans` is constructed as follows: if `n` is even, it consists of the first `n // 2` uppercase letters of the alphabet, each repeated twice (e.g., 'AABBCC' for `n = 6`). If `n` is odd, it starts with 'AAA' and then continues with the first `n // 2 - 1` uppercase letters of the alphabet, each repeated twice (e.g., 'AAABBC' for `n = 5`). The function does not modify any external state beyond printing to the console.

