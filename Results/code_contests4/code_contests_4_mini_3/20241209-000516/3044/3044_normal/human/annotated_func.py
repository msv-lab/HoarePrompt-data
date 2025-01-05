#State of the program right berfore the function call: The input consists of a single integer n (1 ≤ n ≤ 50) followed by n lines, each containing either the command "pwd" or the command "cd" with a non-empty parameter that includes lowercase Latin letters, slashes, and dots. The command parameter does not end with a slash unless it is the root directory, and its length is from 1 to 200 characters.
def func():
    cur = []
    for i in range(int(input())):
        s = raw_input()
        
        if s == 'pwd':
            print('/' + '/'.join(cur))
        else:
            s = s.split()[1]
            if s[0] == '/':
                cur = []
                s = s[1:]
            for x in s.split('/'):
                if x == '..':
                    cur = cur[:-1]
                else:
                    cur.append(x)
        
    #State of the program after the  for loop has been executed: `cur` is a list containing the valid non-empty segments from all inputs processed, excluding any segments that are '..', `i` is the total number of iterations executed, and `s` is the last input string processed. If the last input was 'pwd', the printed output is '/'.
#Overall this is what the function does:The function processes a series of commands that simulate navigation in a file system. It accepts a number of commands, where "pwd" outputs the current directory as a path, and "cd <directory>" changes the current directory according to the specified path. The function handles absolute paths by resetting the current path and supports navigation with ".." to move up one directory level. The valid segments are stored in a list, which represents the current directory structure. If the "pwd" command is issued, it prints the current path; otherwise, the current path is updated based on "cd" commands. The function does not return any value. It assumes the input follows the specified format and does not handle invalid commands or parameters.

