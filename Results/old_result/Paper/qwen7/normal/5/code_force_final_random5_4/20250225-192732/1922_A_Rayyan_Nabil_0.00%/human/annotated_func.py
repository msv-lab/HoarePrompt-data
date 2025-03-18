#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is a positive integer such that 1 ≤ n ≤ 20, and a, b, and c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: `i` is `n`, `t` is `0`, `l` is 'YES', `b` is an input from the user, `c` is an input from the user.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) indicating the number of test cases to follow, and for each test case, three strings \( a \), \( b \), and \( c \) of equal length \( n \). It checks whether for every position \( i \) in the strings, either \( a[i] \) equals \( c[i] \) or \( b[i] \) equals \( c[i] \). If this condition holds for all positions in any test case, the function prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function concludes.

