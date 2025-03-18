#State of the program right berfore the function call: The function should take three parameters: an integer n, and three strings a, b, and c. n is a positive integer (1 ≤ n ≤ 20), and each of the strings a, b, and c consists of exactly n lowercase Latin letters.
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
        
    #State: The loop will execute `t` times, and for each iteration, it will read `n`, `a`, `b`, and `c` from the input. After processing these inputs, it will print 'YES' if the conditions for `match_a_b` and `match_c` are met, otherwise it will print 'NO'. The variables `n`, `a`, `b`, `c`, `template`, `match_a_b`, and `match_c` will be reset for each iteration of the loop.
#Overall this is what the function does:The function reads a series of test cases from the input. For each test case, it takes three strings `a`, `b`, and `c` of equal length `n` (1 ≤ n ≤ 20) and checks if `a` and `b` can be transformed into a common template string where characters that differ between `a` and `b` are uppercased. It then checks if `c` matches this template string. If `a` and `b` match the template and `c` does not, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value.

