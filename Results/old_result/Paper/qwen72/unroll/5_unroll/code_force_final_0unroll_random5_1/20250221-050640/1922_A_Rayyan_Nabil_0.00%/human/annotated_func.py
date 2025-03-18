#State of the program right berfore the function call: The function `func` is expected to be called within a context where the input is provided in a specific format, which includes an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and for each test case, an integer n (1 ≤ n ≤ 20) representing the length of the strings, followed by three strings a, b, and c, each consisting of exactly n lowercase Latin letters.
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
        
    #State: The value of `l` will be 'NO' for each test case, as the `else` block of the inner loop sets `l` to 'NO' after the loop completes without encountering a `break` statement. The value of `t` will be unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and three strings `a`, `b`, and `c` of length `n`. It checks if for every index `i` in the range of `n`, either `a[i]` or `b[i]` matches `c[i]`. If this condition is met for all indices, it prints 'YES' for that test case; otherwise, it prints 'NO'. The function does not return any value. After the function concludes, the value of `t` remains unchanged, and the value of `l` will be 'NO' for each test case, as the `else` block of the inner loop sets `l` to 'NO' after the loop completes without encountering a `break` statement.

