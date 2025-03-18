#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is a positive integer such that 1 ≤ n ≤ 20, and a, b, and c are strings consisting of exactly n lowercase Latin letters.
def func():
    t = int(input())
    l = 'YES'
    for i in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        for i in range(n):
            if a[i] != c[i] and b[i] != c[i]:
                l = 'YES'
        else:
            l = 'NO'
        
        print(l)
        
    #State: Output State: `t` is a positive integer between 1 and 1000 (inclusive), `l` is either 'YES' or 'NO', `n` remains unchanged, `a` remains unchanged, `b` remains unchanged, `c` remains unchanged.
    #
    #After the loop executes all the iterations, the value of `l` will be determined based on the conditions inside the nested loop. If for any string `i` from `n`, the characters at that position in `a` and `b` do not match the character at the same position in `c`, then `l` will be set to 'YES'. Otherwise, if no such positions exist, `l` will be set to 'NO'.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads three strings `a`, `b`, and `c`, each of length `n` (where 1 ≤ n ≤ 20). It checks if for every position `i` from 0 to `n-1`, the characters in `a[i]` and `b[i]` both match the character in `c[i]`. If there exists at least one position where this condition is not met, it sets `l` to 'YES'; otherwise, it sets `l` to 'NO'. After processing all test cases, it prints the value of `l` for each case.

