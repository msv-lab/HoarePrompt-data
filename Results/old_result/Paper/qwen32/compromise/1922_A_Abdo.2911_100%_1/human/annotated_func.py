#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, for each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: The loop will have executed `t` times, and for each execution, it will have printed either 'YES' or 'NO' based on the conditions specified. `t` will be 0, and `n`, `a`, `b`, and `c` will retain their most recently assigned values from the last iteration.
#Overall this is what the function does:The function `func_1` processes `t` test cases, where each test case consists of three strings `a`, `b`, and `c` of length `n` (with `1 ≤ n ≤ 20`). For each test case, it determines if there exists at least one position `i` where the character in `c` is different from the characters in both `a` and `b` at the same position. If such a position exists, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function terminates.

