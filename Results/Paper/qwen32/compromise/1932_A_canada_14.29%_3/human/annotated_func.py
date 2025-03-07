#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n is an integer such that 1 <= n <= 50, and the path is a string of length n consisting of characters '.', '@', and '*', where the first character is guaranteed to be '.'.
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
        
    #State: The output state after all iterations is the sequence of values of `ret` printed for each test case, where `ret` is the count of '@' characters encountered in the string `s` before two consecutive '*' characters are seen.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string of characters '.', '@', and '*'. For each test case, it counts the number of '@' characters encountered before the appearance of two consecutive '*' characters and prints this count.

