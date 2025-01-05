#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and each command is either "pwd" or "cd" followed by a space-separated non-empty parameter consisting of lowercase Latin letters, slashes, and dots, with the command parameter having a length from 1 to 200 characters inclusive.
def func_3():
def func():
    return map(int, input().split())
    cur = []
    #The program returns a map object containing integers parsed from the input sequence split by spaces
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 50) and processes a series of commands that are either "pwd" or "cd" followed by a path. It maintains a current directory state in a list, updating it based on the commands. The "pwd" command outputs the current directory path, while the "cd" command modifies the current directory based on the provided path segments, handling absolute and relative paths, as well as navigating up directories with "..". The function does not return any value directly; instead, it prints the current directory path when "pwd" is invoked.

