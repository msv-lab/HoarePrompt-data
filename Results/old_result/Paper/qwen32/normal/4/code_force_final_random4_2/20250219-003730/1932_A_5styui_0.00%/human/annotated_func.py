#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 50, and the path is a string of length n consisting of characters '.', '@', or '*', where the first character is '.'.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000; `n` is an integer such that 1 <= n <= 50; `path` is a string of length `n` consisting of characters '.', '@', or '*', where the first character is '.'; `a` is an input integer; `d` is the last input integer read; `b` is the last input string read; `i` is equal to `a`; `j` is the index at which the inner loop breaks in the last iteration or the length of `b` if the loop completes all iterations; `s` is 0.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `path` of length `n`. The string `path` consists of characters '.', '@', or '*', with the first character guaranteed to be '.'. The function counts the number of '@' characters in the string `path` for each test case and prints this count. After processing each test case, the count is reset to zero.

