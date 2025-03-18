#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        possible = False
        
        for i in range(n):
            if a[i] == b[i]:
                if c[i] != a[i]:
                    possible = True
                    break
            elif c[i] == a[i] or c[i] == b[i]:
                continue
            else:
                possible = True
                break
        
        if possible:
            print('YES')
        else:
            print('NO')
        
    #State: The loop will print 'YES' or 'NO' for each of the `t` iterations.
#Overall this is what the function does:The function `func_1` processes `t` test cases, each consisting of three strings `a`, `b`, and `c` of length `n`. For each test case, it determines if there exists at least one position where the character in `c` does not match the character in either `a` or `b`, and prints 'YES' if such a position exists, otherwise 'NO'.

