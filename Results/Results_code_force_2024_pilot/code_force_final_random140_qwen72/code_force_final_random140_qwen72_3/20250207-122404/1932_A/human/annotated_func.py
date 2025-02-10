#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, representing the number of test cases. For each test case, n is an integer such that 1 <= n <= 50, representing the length of the path. The path is represented by a string of n characters where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The first cell of the path is always empty ('.').
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
                thorn = 0
        
        print(ret)
        
    #State: After the loop executes all the iterations, the variable `ret` holds the total number of '@' characters encountered in the path string `s` before encountering two consecutive '*' characters. The variable `thorn` will be 2 if two consecutive '*' characters were encountered, causing the inner loop to break. The variable `len` remains the same as the input integer, and the list `s` remains unchanged as the list of characters from the input string. The variable `_` (the loop counter) will have completed its range, meaning it has iterated `t` times, where `t` is the number of test cases.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n` and a string `s` representing a path. The path consists of characters '.', '@', and '*', with the first character always being '.'. For each test case, the function counts the number of '@' characters encountered in the path until it encounters two consecutive '*' characters, at which point it stops counting. The function prints the count for each test case. The function does not return any value; instead, it directly outputs the result for each test case. After processing all test cases, the function terminates.

