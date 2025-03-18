#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: The loop has executed `t` times, `i` is `n - 1 + t`, `n` is the final value of `t + (n-1) * (number of iterations)`, and `possible` is either `True` or `False`.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer `t` (1 ≤ t ≤ 1000), an integer `n` (1 ≤ n ≤ 20), and three strings `a`, `b`, and `c` (each consisting of exactly `n` lowercase Latin letters). For each test case, it checks if it's possible to transform string `c` into either string `a` or `b` by changing exactly one character at the same position. If such a transformation is possible, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

