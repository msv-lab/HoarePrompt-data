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
        
    #State: Output State: t is an integer between 1 and 1000 (inclusive), n, a, b, and c are strings of equal length n, where each character in a, b, and c is either a lowercase or uppercase letter. For each iteration of the loop, if the conditions specified in the code are met, 'YES' is printed; otherwise, 'NO' is printed. The final output state is determined by the cumulative output of all iterations, with 'YES' or 'NO' printed for each iteration.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer t (number of test cases), an integer n (length of strings), and three strings a, b, and c (each of length n). For each test case, it constructs a template string based on the comparison of characters in a and b. It then checks if the template matches a and b but does not match c. If the conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The final output consists of 'YES' or 'NO' for each test case.

