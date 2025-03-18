#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 50, and the path is a string of n characters where each character is either '.', '@', or '*', and the first character is always '.'.
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
        
    #State: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 50, path is a string of n characters where each character is either '.', '@', or '*' and the first character is always '.', a is an input integer, s is 0.
#Overall this is what the function does:The function `func` reads an integer `a` from the user, then for each of the `a` iterations, it reads another integer `d` and a string `b` from the user. It counts the number of '@' characters in `b` and prints this count. If a '*' character is encountered in `b`, the counting process stops immediately. After processing each iteration, the count is reset to 0. The function does not return any value. After the function concludes, `t` and `n` remain unchanged, `path` is unchanged, and `a` is the last input integer read by the function.

