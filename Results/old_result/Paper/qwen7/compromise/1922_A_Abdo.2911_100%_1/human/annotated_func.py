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
        
    #State: The loop has executed `t` times, where `t` is the initial value of `t` provided by `int(input())`. For each iteration, the variable `i` is set to `n` (the length of strings `a`, `b`, and `c`), `n` is a positive integer, and `possible` is either `True` or `False` based on the conditions checked within the loop. If `possible` turned `True` for any of the `n` iterations, it remains `True`; otherwise, it remains `False`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers t and n, and strings a, b, and c. It then checks if it's possible to transform string c into either string a or b by changing one character at a time. If such a transformation is possible, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

