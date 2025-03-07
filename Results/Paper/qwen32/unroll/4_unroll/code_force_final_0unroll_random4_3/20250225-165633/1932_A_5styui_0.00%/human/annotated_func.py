#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 50, and the path is a string of n characters where each character is either '.', '@', or '*', and the first character of the path is '.'.
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
        
    #State: t is an integer such that 1 <= t <= 1000; for each test case, n is an integer such that 1 <= n <= 50, and path is a string of n characters where each character is either '.', '@', or '*', and the first character of path is '.'; a is an input integer; s is 0.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a string of characters ('.', '@', or '*'). It counts the number of '*' characters encountered before the first '@' character in each string. If there is no '@' character, it counts all '*' characters in the string. The result for each test case is printed.

