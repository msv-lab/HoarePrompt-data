#State of the program right berfore the function call: The function should take four parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and for each test case, an integer n (1 ≤ n ≤ 20) representing the length of the strings, and three strings a, b, and c, each consisting of exactly n lowercase Latin letters.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        possible = False
        
        for i in range(n):
            if a[i] == b[i]:
                if c[i] != a[i]:
                    possible = True
                    break
            elif c[i] == a[i] or c[i] == b[i]:
                continue
            else:
                possible = True
                break
        
        if possible:
            print('YES')
        else:
            print('NO')
        
    #State: `t` is 0, `n` is an input integer, `a`, `b`, and `c` are user inputs with leading and trailing spaces removed, `i` is `n-1`. If `possible` is True, it indicates that at least one character in `c` is not equal to the corresponding character in `a` or `b` (and `a[i]` is not equal to `b[i]`), or there exists at least one character in `a` that is equal to the corresponding character in `b` and the corresponding character in `c` is different. If `possible` is False, it indicates that all characters in `c` are equal to the corresponding characters in `a` and `b` (and `a[i]` is equal to `b[i]`).
#Overall this is what the function does:The function `func_1` reads multiple test cases from the user input. For each test case, it reads an integer `n` and three strings `a`, `b`, and `c` of length `n`. It checks if there is any index `i` where the character in `c` is different from the corresponding characters in `a` and `b` when `a[i]` is equal to `b[i]`, or if `c[i]` is different from both `a[i]` and `b[i]` when `a[i]` is not equal to `b[i]`. If such a condition is met, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function concludes with `t` being 0, `n` being the last input integer, and `a`, `b`, and `c` being the last input strings with leading and trailing spaces removed. The variable `i` is set to `n-1` and `possible` is either True or False based on the conditions checked.

