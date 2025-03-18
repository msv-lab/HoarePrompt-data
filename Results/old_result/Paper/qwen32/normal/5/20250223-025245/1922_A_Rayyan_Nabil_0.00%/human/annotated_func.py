#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, for each test case n is an integer such that 1 <= n <= 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: t is an integer such that 1 <= t <= 1000, i is n, n is the newly input integer, a is the newly input string, b is the newly input string, c is the newly input string, and l is 'YES' if there exists at least one index i such that a[i] != c[i] and b[i] != c[i] for each of the t test cases; otherwise, l is 'NO' for that test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and three strings `a`, `b`, and `c`, each of length `n`. It then checks if there exists at least one index `i` such that `a[i]` is not equal to `c[i]` and `b[i]` is not equal to `c[i]`. If such an index exists for a test case, it prints 'YES'; otherwise, it prints 'NO'.

