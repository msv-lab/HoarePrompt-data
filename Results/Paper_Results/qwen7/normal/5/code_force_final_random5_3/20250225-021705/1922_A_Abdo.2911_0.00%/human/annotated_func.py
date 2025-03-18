#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: Output State: All iterations of the loop have been executed, with the following conditions met:
    #- The variable `t` contains the total number of iterations the loop ran.
    #- For each iteration, `n` is the length of the strings `a`, `b`, and `c`.
    #- After processing all strings, `template` is a list of characters derived from string `a` such that:
    #  - Characters in `template` are either identical to those in `a` or converted to uppercase if they differ from corresponding characters in `b`.
    #  - `match_a_b` is True if the characters in `template` exactly match the characters in `a` when both are considered in lowercase, and also match the characters in `b` when both are considered in lowercase.
    #  - `match_c` is True if the characters in `template` exactly match the characters in `c` when both are considered in lowercase, and False otherwise.
    #- The final output will be 'YES' if `match_a_b` is True and `match_c` is False, and 'NO' otherwise.
    #
    #This means that after all iterations, the program will check if the processed `template` matches `a` and `b` in a specific way and does not match `c`. If these conditions are satisfied, it prints 'YES', otherwise 'NO'.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes an integer `t` representing the number of iterations, an integer `n` indicating the length of strings `a`, `b`, and `c`, and two strings `a` and `b`, and one string `c`, all consisting of exactly `n` lowercase Latin letters. For each test case, it constructs a template from string `a` by converting differing characters to uppercase. Then, it checks if the template matches `a` and `b` under specific conditions but does not match `c`. If these conditions are met, it prints 'YES'; otherwise, it prints 'NO'.

