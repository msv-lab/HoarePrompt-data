#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: A series of 'YES' and 'NO' printed to the console, determined by the conditions `match_a_b` and `match_c` for each iteration of the loop.
#Overall this is what the function does:The function `func_1` processes a series of test cases, each consisting of three strings `a`, `b`, and `c` of equal length `n`. For each test case, it determines if the string `c` matches a specific template derived from `a` and `b`. The template is created by comparing characters at each position in `a` and `b`; if they match, the character is added in lowercase; if they differ, the character from `a` is added in uppercase. The function then checks if `a` and `b` strictly adhere to this template (lowercase characters must match exactly, and uppercase characters must not match either `a` or `b` at that position), and if `c` does not match the template in the same way `a` and `b` do. If these conditions are met, it prints 'YES'; otherwise, it prints 'NO'.

