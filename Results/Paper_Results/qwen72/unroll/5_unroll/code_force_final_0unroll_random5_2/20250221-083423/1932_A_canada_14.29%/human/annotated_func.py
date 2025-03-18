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
        
    #State: The value of `ret` will be the number of '@' characters encountered in the string `s` before the first occurrence of two consecutive '*' characters. The values of `t`, `n`, and `path` remain unchanged.
#Overall this is what the function does:The function `func` processes a series of inputs where each input consists of an integer `len` and a string `s` of length `len`. The function counts the number of '@' characters in `s` until it encounters two consecutive '*' characters, at which point it stops counting. The function then prints the count of '@' characters for each input. The function does not return any value and does not modify the global state or the input parameters `t`, `n`, and `path` (if they exist outside the function).

