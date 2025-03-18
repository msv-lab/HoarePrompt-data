#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 20. a, b, and c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' printed based on the conditions specified in the loop. For each iteration, if the conditions `match_a_b` and `not match_c` are met, 'YES' is printed; otherwise, 'NO' is printed. The exact sequence of 'YES' and 'NO' depends on the inputs provided during each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer \( t \) (number of test cases), an integer \( n \) (length of strings), and three strings \( a \), \( b \), and \( c \) (each of length \( n \) consisting of lowercase Latin letters). For each test case, it constructs a template string based on the comparison between \( a \) and \( b \), then checks if \( a \) and \( b \) match according to the template and if \( c \) does not match the template. If \( a \) and \( b \) match the template but \( c \) does not, it prints 'YES'; otherwise, it prints 'NO'. The function outputs a series of 'YES' and 'NO' based on these conditions for each test case.

