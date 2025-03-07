#State of the program right berfore the function call: The function should take an integer t and a list of integers n, where 1 <= t <= 50 and for each n in the list, 1 <= n <= 50.
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
        
    #State: The variable `t` is unchanged. The variable `s` remains 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. For each iteration of the loop, if the input `n` is 1, 'NO' is printed. For all other values of `n`, 'YES' is printed followed by a string `ans` that is constructed as follows: if `n` is even, `ans` is a string where each character from 'A' to the character corresponding to the index `n // 2 - 1` in `s` is repeated twice. If `n` is odd, `ans` starts with 'AAA' and then each character from 'B' to the character corresponding to the index `n // 2 - 1` in `s` is repeated twice.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It interacts with the user to clear the console screen, then prompts the user to input an integer `t` (1 <= t <= 50). For each of the `t` iterations, it prompts the user to input another integer `n` (1 <= n <= 50). If `n` is 1, it prints 'NO'. If `n` is greater than 1, it prints 'YES' followed by a string `ans`. The string `ans` is constructed such that if `n` is even, each character from 'A' to the character corresponding to the index `n // 2 - 1` in the uppercase English alphabet is repeated twice. If `n` is odd, `ans` starts with 'AAA' and then each character from 'B' to the character corresponding to the index `n // 2 - 1` in the uppercase English alphabet is repeated twice. The function does not modify any external state or variables.

