#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: `i` is equal to `n`, `n` is greater than 0, `possible` is `True`, `a`, `b`, and `c` are the input strings stripped of whitespace, and `t` is greater than 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (number of cases), an integer n (length of strings), and three strings a, b, and c (each of length n). For each test case, it checks if it's possible to rearrange string c into either string a or b by swapping characters. If such a rearrangement is possible, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

