#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, for each test case n is an integer such that 1 <= n <= 20, and a, b, c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: l is 'YES' or 'NO' based on the last test case.
#Overall this is what the function does:The function processes `t` test cases, each consisting of an integer `n` and three strings `a`, `b`, and `c` of length `n`. For each test case, it checks if every character in string `c` matches at least one of the corresponding characters in strings `a` or `b`. It prints 'YES' if this condition is met for all characters in `c` for a given test case, otherwise it prints 'NO'.

