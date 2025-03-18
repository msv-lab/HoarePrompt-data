#State of the program right berfore the function call: The function `func_1` is expected to take four parameters: `t`, `n`, `a`, `b`, and `c`. `t` is an integer representing the number of test cases, where 1 ≤ t ≤ 1000. `n` is an integer representing the length of the strings `a`, `b`, and `c`, where 1 ≤ n ≤ 20. `a`, `b`, and `c` are strings consisting of exactly `n` lowercase Latin letters.
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
        
    #State: The loop has finished executing all `t` iterations, and the final state is that `t` is an input integer where 1 ≤ t ≤ 1000; `n` is an integer representing the length of the strings `a`, `b`, and `c`, where 1 ≤ n ≤ 20; `a`, `b`, and `c` are strings consisting of exactly `n` lowercase Latin letters. The variables `template`, `match_a_b`, and `match_c` are not retained after each iteration, so they do not have a final state outside the loop. The loop prints 'YES' or 'NO' for each iteration based on the conditions checked.
#Overall this is what the function does:The function `func_1` reads input from the user to process `t` test cases, where `t` is an integer (1 ≤ t ≤ 1000). For each test case, it reads three strings `a`, `b`, and `c` of length `n` (1 ≤ n ≤ 20) consisting of lowercase Latin letters. The function checks if the strings `a` and `b` can be transformed into a common template string, where characters that differ between `a` and `b` are marked as uppercase in the template. It then checks if the string `c` matches this template, with the condition that any lowercase character in the template must match the corresponding character in `c`, and any uppercase character in the template must not match the corresponding character in `c`. If the conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value.

