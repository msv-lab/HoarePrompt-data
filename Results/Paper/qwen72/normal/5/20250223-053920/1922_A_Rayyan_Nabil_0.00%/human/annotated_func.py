#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 20) and three strings a, b, and c, each of length n and consisting of lowercase Latin letters. The function should determine if there exists a template t such that strings a and b match t, while string c does not.
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
        
    #State: The variable `l` will be 'NO' for each test case after the loop executes all the iterations, because the `else` block of the inner loop is executed only if the loop completes without encountering a `break` statement, and in this case, it will always set `l` to 'NO' after checking all characters.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and three strings `a`, `b`, and `c`, each of length `n`. The function checks if there exists at least one character position `i` (0 ≤ i < n) where `a[i]` or `b[i]` is different from `c[i]`. If such a position exists, it prints 'YES' for that test case; otherwise, it prints 'NO'. The function does not return any value.

