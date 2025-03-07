#State of the program right berfore the function call: The function should take three parameters: an integer n, and three strings a, b, and c. n is a positive integer such that 1 <= n <= 20, and a, b, and c are strings of exactly n lowercase Latin letters.
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
        
    #State: The loop will execute t times, and for each iteration, it will read n, a, b, and c from the input. After processing, it will print 'YES' if the conditions for matching a and b with the template are met and c does not match the template, otherwise it will print 'NO'. The variables n, a, b, and c will be overwritten in each iteration, and their final values will be the values from the last iteration. The template list will be reset and recalculated in each iteration, so its final state will be the result of the last iteration's calculations.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the input, indicating the number of test cases. For each test case, it reads three inputs: an integer `n` (1 <= n <= 20), and three strings `a`, `b`, and `c` (each of length `n` and containing lowercase Latin letters). It then processes these inputs to determine if a specific condition is met: the strings `a` and `b` must match a generated template, and the string `c` must not match this template. The template is constructed by comparing characters of `a` and `b` and using uppercase characters where they differ. If the condition is met, the function prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. After processing all test cases, the final state of the program is that the variables `n`, `a`, `b`, and `c` will hold the values from the last test case, and the template list will be the result of the last test case's calculations.

