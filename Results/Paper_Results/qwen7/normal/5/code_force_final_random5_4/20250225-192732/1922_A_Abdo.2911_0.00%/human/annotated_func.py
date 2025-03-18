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
        
    #State: Output State: `match_a_b` is either `True` or `False`, `match_c` is either `True` or `False`, `i` is `3`, and `n` is greater than `3`.
    #
    #Explanation: After all iterations of the loop, the values of `match_a_b` and `match_c` will depend on the conditions checked within the loops. The variable `i` will be set to `3` because it is incremented in the innermost loop, which runs up to `n-1`, and the loop iterates `t` times. Since `t` is the input integer and we know it is between 1 and 1000, `n` (which is the length of string `a`) will be greater than `3` as per the given conditions after three iterations. The final values of `match_a_b` and `match_c` will reflect whether the conditions specified in the loop were met for all inputs processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \) (number of test cases, 1 ≤ \( t \) ≤ 1000), an integer \( n \) (length of strings, 1 ≤ \( n \) ≤ 20), and three strings \( a \), \( b \), and \( c \) (each of length \( n \) and containing only lowercase Latin letters). For each test case, it constructs a template string based on the comparison of \( a \) and \( b \), checks if \( a \) and \( b \) match according to the template, and then checks if \( c \) matches the template. If \( a \) and \( b \) match but \( c \) does not, the function prints 'YES'; otherwise, it prints 'NO'.

