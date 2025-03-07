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
        
    #State: _ is t-1, t is an integer between 1 and 1000, n is an input integer greater than 0, a, b, and c are input strings with leading and trailing whitespace removed, i is n-1. If `possible` is True, it means that at least one of the following conditions has been met during the loop execution for any of the test cases: (1) a[i] == b[i] and c[i] != a[i], or (2) a[i] != b[i] and c[i] != a[i] and c[i] != b[i]. If `possible` is False, none of these conditions have been met during the loop execution for any of the test cases.
#Overall this is what the function does:The function `func_1` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and three strings `a`, `b`, and `c` of length `n`. The function checks if there is any index `i` where either `a[i] == b[i]` and `c[i] != a[i]`, or `a[i] != b[i]` and `c[i]` is different from both `a[i]` and `b[i]`. If such an index is found for any test case, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function completes without returning any value.

