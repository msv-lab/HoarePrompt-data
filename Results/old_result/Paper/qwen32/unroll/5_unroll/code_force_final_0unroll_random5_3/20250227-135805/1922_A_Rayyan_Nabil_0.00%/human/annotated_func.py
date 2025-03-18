#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: l is 'YES' or 'NO' based on the last test case's strings a, b, and c.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and three strings `a`, `b`, and `c`, each of length `n`. It then checks if for each position `i` in the strings, at least one of `a[i]` or `b[i]` matches `c[i]`. If this condition holds for all positions in the last test case, it prints 'YES'; otherwise, it prints 'NO'.

