#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 20. The strings a, b, and c are each of length n and consist of exactly n lowercase Latin letters.
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
        
    #State: A series of 'YES' or 'NO' responses for each of the `t` test cases.
#Overall this is what the function does:The function `func_1` processes `t` test cases, each consisting of three strings `a`, `b`, and `c` of length `n`. For each test case, it determines if the string `c` matches a specific pattern derived from `a` and `b`. The pattern requires that for each position, if `a` and `b` have the same character, `c` must also have the same character; if `a` and `b` differ, `c` must not have the same character as either `a` or `b` at that position. The function outputs 'YES' if `c` matches the pattern and 'NO' otherwise.

