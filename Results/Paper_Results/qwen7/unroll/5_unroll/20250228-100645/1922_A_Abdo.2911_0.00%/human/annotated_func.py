#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: Output State: The output state will consist of 'YES' or 'NO' printed for each iteration of the loop based on the conditions specified in the loop body. For each input value of `t`, the program will process `n` characters from strings `a`, `b`, and `c`. If the processed template matches `a` and `b` but not `c`, it will print 'YES'; otherwise, it will print 'NO'. The final output state will be a series of 'YES' or 'NO' results corresponding to each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers t and n, and strings a, b, and c. It constructs a template based on the comparison between strings a and b. Then, it checks if the template matches a and b but does not match c. If the conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The final output consists of 'YES' or 'NO' for each test case.

