#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 50) and a string of n characters representing the path. The string consists of '.', '@', and '*' characters, where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The first cell of each path is guaranteed to be empty ('.').
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
        
    #State: For each test case, the loop will output the number of coins ('@') collected before encountering two consecutive thorns ('*'). If two consecutive thorns are encountered, the loop will stop and print the count of coins collected up to that point. The loop will execute for each test case and print the result for each one.
#Overall this is what the function does:The function `func` reads input from the user, where the first input is an integer `t` (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 50) and a string `s` of `n` characters representing a path. The path consists of '.', '@', and '*' characters, where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The function then processes each path and prints the number of coins ('@') collected before encountering two consecutive thorns ('*'). If two consecutive thorns are encountered, the function stops processing the current path and prints the count of coins collected up to that point. The function does not return any value; it only prints the results for each test case.

