#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 50, and the path is a string of n characters where each character is either '.', '@', or '*', and the first character is '.'.
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
        
    #State: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 50, and the path is a string of n characters where each character is either '.', '@', or '*', and the first character is '.'. For each iteration of the loop, the variable `ret` will contain the number of '@' characters encountered before the first occurrence of two consecutive '*' characters, and `thorn` will be 0 or 1 depending on whether a single '*' has been encountered or not. The loop will print the value of `ret` for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case involves a string `s` of up to 50 characters consisting of '.', '@', or '*'. For each test case, it counts the number of '@' characters encountered before the first occurrence of two consecutive '*' characters. It prints this count for each test case and does not return any value. The state of the program after the function concludes is that `t` test cases have been processed, and the counts of '@' characters for each test case have been printed. The input variables `t`, `n`, and `s` are not modified.

