#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: Output State: After all iterations of the loop have finished, `match_c` will be either True or False, `i` will be equal to `n`, and `n` will be greater than 0. Additionally, either both `match_a_b` and `match_c` will be True, or `match_a_b` will be False.
    #
    #This means that after all iterations, the loop has processed all given inputs (`t` times), and for each iteration, it has checked if `template` matches `a` and `b` under certain conditions and compared `template` with `c`. The final values of `match_a_b` and `match_c` depend on these comparisons across all iterations. If `match_a_b` is True and `match_c` is False for any iteration, `match_c` will remain False. Otherwise, `match_c` will be True if there is no such condition.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer t (1 ≤ t ≤ 1000), an integer n (1 ≤ n ≤ 20), and three strings a, b, and c, each consisting of exactly n lowercase Latin letters. For each test case, it constructs a template string based on the comparison of a and b. It then checks if the template matches a and b under specific conditions and compares the template with c. Finally, it prints 'YES' if the template matches a and b but not c, and 'NO' otherwise. The function does not return any value but prints the result for each test case.

