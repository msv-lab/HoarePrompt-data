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
        
    #State: the value of `l` after the last iteration of the outer loop, which is either 'YES' or 'NO' depending on the input strings `a`, `b`, and `c` in the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three strings `a`, `b`, and `c` of equal length. For each test case, it checks if each character in string `c` matches at least one of the corresponding characters in strings `a` or `b`. If this condition is met for all characters in `c`, it outputs 'YES'; otherwise, it outputs 'NO'.

