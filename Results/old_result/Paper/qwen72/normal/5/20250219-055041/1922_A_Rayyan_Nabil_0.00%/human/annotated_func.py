#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, n is an integer where 1 <= n <= 20, a, b, and c are strings of length n consisting of lowercase Latin letters.
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
        
    #State: `t` is 0, `i` is `n-1`, `n` is a positive integer, `a`, `b`, and `c` are strings of length `n` consisting of lowercase Latin letters, and `l` is 'NO' or 'YES'. For each iteration, if any character at index `i` in `a` is not equal to the corresponding character in `c` and the character at index `i` in `b` is also not equal to the corresponding character in `c`, then `l` is 'YES'. Otherwise, `l` remains 'NO'.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n` and three strings `a`, `b`, and `c` from the input, where `n` is the length of the strings and all strings consist of lowercase Latin letters. The function then checks, for each character position in the strings, if the character in `a` or `b` matches the corresponding character in `c`. If at any position, both `a` and `b` do not match `c`, the function prints 'YES'. Otherwise, it prints 'NO'. After processing all test cases, the function concludes with no return value.

