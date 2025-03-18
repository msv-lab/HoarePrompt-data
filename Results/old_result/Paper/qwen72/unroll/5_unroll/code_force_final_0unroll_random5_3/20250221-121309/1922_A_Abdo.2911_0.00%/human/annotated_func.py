#State of the program right berfore the function call: The function should take four parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and for each test case, an integer n (1 ≤ n ≤ 20) representing the length of the strings, and three strings a, b, and c, each consisting of exactly n lowercase Latin letters.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        template = []
        
        for i in range(n):
            if a[i] == b[i]:
                template.append(a[i])
            else:
                template.append(a[i].upper())
        
        match_a_b = True
        
        for i in range(n):
            if template[i].islower():
                if a[i] != template[i] or b[i] != template[i]:
                    match_a_b = False
                    break
            elif a[i].lower() == template[i].lower() or b[i].lower() == template[i
                ].lower():
                match_a_b = False
                break
        
        match_c = True
        
        for i in range(n):
            if template[i].islower():
                if c[i] != template[i]:
                    match_c = False
                    break
            elif c[i].lower() == template[i].lower():
                match_c = False
                break
        
        if match_a_b and not match_c:
            print('YES')
        else:
            print('NO')
        
    #State: The loop has finished executing all `t` iterations. For each test case, the program has checked if the string `c` matches the template derived from strings `a` and `b` according to the specified rules. If `c` matches the template and `a` and `b` do not conflict with the template, the program has printed 'YES'. Otherwise, it has printed 'NO'. The values of `t`, `n`, `a`, `b`, and `c` are unchanged for each test case, but the loop has processed each test case and printed the corresponding output.
#Overall this is what the function does:The function `func_1` processes a series of test cases. For each test case, it reads an integer `n` and three strings `a`, `b`, and `c`, each of length `n`. It then checks if the string `c` matches a template derived from `a` and `b` according to specific rules: the template is constructed by copying characters from `a` and `b` where they match, and using uppercase characters where they differ. The function prints 'YES' if `c` matches the template and `a` and `b` do not conflict with the template, and 'NO' otherwise. The function does not return any value; it only prints the results for each test case.

