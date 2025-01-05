#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 50) representing the number of commands. Each command is either 'pwd' or 'cd' followed by a space and a non-empty parameter consisting of lowercase Latin letters, slashes, and dots. The command parameter 'cd' does not end with a slash unless it is the root directory represented by a single slash. The length of the command parameter is between 1 and 200 characters inclusive.
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
        
    #State of the program after the  for loop has been executed: `cur` is a list of valid directory names derived from all the inputs processed, excluding any that were removed by '..'; if no valid input was provided, `cur` remains an empty list.
#Overall this is what the function does:The function processes a series of filesystem commands, specifically 'pwd' and 'cd', to manage the current working directory. It prints the current directory path when 'pwd' is called, and updates the directory based on 'cd' commands, handling both relative and absolute paths, as well as the special case of going up one directory with '..'. If the 'cd' command is provided with a root directory ('/'), it resets the current directory to the root. The function does not take any parameters, and it assumes valid input based on the constraints described in the comments.

