#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 50, and the path is a string of n characters where each character is either '.', '@', or '*', and the first character is '.'.
def func():
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if b[:]:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 50, path is a string of n characters where each character is either '.', '@', or '*' and the first character is '.', a is an input integer, s is 0.
#Overall this is what the function does:The function `func` reads an integer `a` from the user, which represents the number of test cases. For each test case, it reads an integer `d` and a string `b` from the user. The string `b` is expected to contain characters '.', '@', or '*'. The function counts the number of '@' characters in `b` until it encounters a '*', at which point it stops counting and breaks out of the loop. After processing each test case, it prints the count of '@' characters and resets the count to 0. The function does not return any value. After the function concludes, the initial parameters `t`, `n`, and `path` remain unchanged, and the function has printed the count of '@' characters for each test case.

