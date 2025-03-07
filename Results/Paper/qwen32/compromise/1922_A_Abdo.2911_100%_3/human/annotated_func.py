#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, for each test case n is an integer such that 1 ≤ n ≤ 20, and a, b, c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: t is 0, n is the last integer value provided by the user, a, b, and c are the last strings of exactly n lowercase Latin letters provided by the user, and possible is True if any condition within the loop was met during any iteration, otherwise False.
#Overall this is what the function does:The function `func_1` processes `t` test cases, each consisting of an integer `n` and three strings `a`, `b`, and `c` of length `n`. For each test case, it checks if there is any position `i` where the character in `c` does not match the character in either `a` or `b` if `a[i]` and `b[i]` are the same, or if `c[i]` does not match either `a[i]` or `b[i]` if they are different. It prints 'YES' if such a position exists for any test case, otherwise it prints 'NO'.

