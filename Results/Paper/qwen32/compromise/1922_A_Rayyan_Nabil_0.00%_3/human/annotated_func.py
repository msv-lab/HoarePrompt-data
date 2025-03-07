#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: the value of `l` after the last iteration
#Overall this is what the function does:The function processes multiple test cases, each consisting of three strings of equal length, and determines for each test case whether there exists at least one position where the characters in the first two strings differ from the character in the third string. If such a position exists for all characters in the strings, it outputs "YES"; otherwise, it outputs "NO".

