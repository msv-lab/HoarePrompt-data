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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `_` is `t - 1`, `n` is the last input integer, `a` is the last input string with leading and trailing whitespace removed, `b` is the last input string with leading and trailing whitespace removed, `c` is the last input string with leading and trailing whitespace removed, `i` is `n - 1`, and `possible` is True if at any point during the last iteration of the loop, either `a[i] == b[i]` and `c[i] != a[i]`, or `a[i] != b[i]` and `c[i]` is not equal to either `a[i]` or `b[i]`. Otherwise, `possible` is False.
#Overall this is what the function does:The function `func_1` reads an integer `t` (1 ≤ t ≤ 1000) from the input, representing the number of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 20) and three strings `a`, `b`, and `c` (each of length `n` and consisting of lowercase Latin letters). The function then checks if there is any index `i` in the range [0, n-1] where either `a[i] == b[i]` and `c[i]` is different from `a[i]`, or `a[i] != b[i]` and `c[i]` is different from both `a[i]` and `b[i]`. If such an index exists, the function prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function completes and the final state of the program includes the variables `t`, `n`, `a`, `b`, `c`, and `possible` as described in the annotations, but the primary effect is the output of 'YES' or 'NO' for each test case.

