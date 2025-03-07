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
        
    #State: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 50, and the path is a string of n characters where each character is either '.', '@', or '*', and the first character is '.'. The variable `ret` will be the number of '@' characters encountered in the string `s` before two consecutive '*' characters are found, and `thorn` will be 0 or 1 depending on whether the last character processed was '*' or not.
#Overall this is what the function does:The function `func` reads input from the user, processes a series of strings, and prints the number of '@' characters encountered in each string before two consecutive '*' characters are found. The function does not return any value. After the function concludes, the state of the program remains unchanged except for the output printed to the console.

