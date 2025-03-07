#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 50, and the path is a string of length n consisting of characters '.', '@', or '*', where the first character is guaranteed to be '.'.
def func():
    for _ in range(int(input())):
        len = int(input())
        
        s = list(input())
        
        ret = 0
        
        thorn = 0
        
        for i in s:
            if i == '@':
                thorn = 0
                ret += 1
            elif i == '*':
                thorn += 1
                if thorn == 2:
                    break
            else:
                thorn == 0
        
        print(ret)
        
    #State: a series of integers where each integer represents the number of '@' characters encountered before two consecutive '*' characters for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a string of characters '.', '@', or '*'. It counts the number of '@' characters encountered before two consecutive '*' characters appear in the string for each test case and outputs this count.

