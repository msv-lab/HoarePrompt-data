#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: `t` is an integer such that `t` is 0; `n` is greater than 0; `a`, `b`, and `c` are string values with leading and trailing whitespace removed; `template` is a list containing the characters of `a` up to the `n`-th character, where each character at index `i` is either `a[i]` or the uppercase version of `a[i]` if `a[i]` is not equal to `b[i]`; `match_a_b` is `True` or `False`; `match_c` is `True` or `False`. The loop has finished executing all `t` iterations, and the final output will have been printed for each iteration.
#Overall this is what the function does:The function `func_1` processes a series of test cases. For each test case, it takes an integer `n` and three strings `a`, `b`, and `c`, each of length `n` consisting of lowercase Latin letters. It then determines if the string `c` matches a specific pattern derived from `a` and `b`, and prints "YES" if `c` matches the pattern and "NO" otherwise. The pattern is such that for each position, if `a` and `b` have the same character, `c` must also have the same character; if `a` and `b` differ, `c` must not have the same character as either `a` or `b` at that position.

