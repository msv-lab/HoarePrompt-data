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
        
    #State: The loop will have executed `t` times, and for each test case, it will have checked the conditions specified in the loop body. If the conditions for a test case result in `possible` being `True`, it will print 'YES' for that test case; otherwise, it will print 'NO'. The variables `t`, `n`, `a`, `b`, and `c` will retain their values after each iteration, but their values will be overwritten in subsequent iterations. After all iterations, `t` will be the same as the initial input, and `n`, `a`, `b`, and `c` will be the values from the last test case.
#Overall this is what the function does:The function `func_1` processes a series of test cases. It accepts an integer `t` (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 20) and three strings `a`, `b`, and `c`, each of length `n` consisting of lowercase Latin letters. The function checks if there is any position `i` in the strings such that `a[i]` is not equal to `b[i]` and `c[i]` is different from both `a[i]` and `b[i]`. If such a position exists, it prints 'YES' for that test case; otherwise, it prints 'NO'. After processing all test cases, the function has printed 'YES' or 'NO' for each test case, and the variables `t`, `n`, `a`, `b`, and `c` will retain the values from the last test case.

