#State of the program right berfore the function call: The function should take three parameters: an integer n, and three strings a, b, and c, where 1 <= n <= 20, and each of a, b, and c consists of exactly n lowercase Latin letters.
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
        
    #State: The loop will execute `t` times, and for each iteration, it will read `n`, `a`, `b`, and `c` from the input. After processing, it will print 'YES' if the conditions for `match_a_b` and `match_c` are met, otherwise it will print 'NO'. The variables `n`, `a`, `b`, and `c` will be overwritten in each iteration, and their final values will be the ones from the last iteration. The `template`, `match_a_b`, and `match_c` variables will be reset and recalculated in each iteration.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the input, indicating the number of test cases. For each test case, it reads an integer `n` and three strings `a`, `b`, and `c`, each of length `n`. It then checks if the strings `a` and `b` match a specific template derived from `a` and `b`, and if `c` does not match this template. If the conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. After processing all test cases, the final values of `n`, `a`, `b`, and `c` will be those from the last test case, and the `template`, `match_a_b`, and `match_c` variables will be in their final state from the last iteration.

