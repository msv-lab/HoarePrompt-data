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
        
    #State: t is 0; n, a, b, and c are the values from the last iteration of the loop.
#Overall this is what the function does:The function `func_1` reads an integer `t` representing the number of test cases. For each test case, it reads three strings `a`, `b`, and `c` of length `n` (where `n` is specified for each test case). It then checks if there exists at least one position `i` in the strings such that `a[i]` is not equal to `b[i]` and `c[i]` is not equal to `a[i]` or `b[i]`. If such a position exists, it prints 'YES'; otherwise, it prints 'NO'.

