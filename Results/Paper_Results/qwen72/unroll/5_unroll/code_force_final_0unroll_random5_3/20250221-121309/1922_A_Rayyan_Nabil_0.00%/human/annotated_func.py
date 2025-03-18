#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 20, and a, b, c are strings of length n consisting of lowercase Latin letters.
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
        
    #State: t is an input integer, 1 <= n <= 20, a, b, c are strings of length n consisting of lowercase Latin letters, l is 'NO'.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads three inputs: an integer `n` (1 <= n <= 20), and two strings `a` and `b` of length `n` consisting of lowercase Latin letters. It then reads another string `c` of the same length. The function checks if for each character position `i` in the strings `a` and `b`, at least one of the characters matches the corresponding character in `c`. If this condition is met for all positions, it prints 'YES'; otherwise, it prints 'NO'. After processing all `t` test cases, the function concludes. The final state of the program is that `t` test cases have been processed, and for each test case, a result ('YES' or 'NO') has been printed based on the input strings.

