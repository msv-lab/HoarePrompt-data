#State of the program right berfore the function call: n is a positive integer. Each command parameter is a non-empty string containing only lowercase Latin letters, slashes, and dots. The length of each command parameter is between 1 and 200 characters.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `cur` contains the final values of `x` where `x` is not equal to '..', and `s` is an empty string.
#Overall this is what the function does:The function `func` reads input commands in a loop, processes them, and updates the `cur` list accordingly. If the command is 'pwd', it prints the current directory path. If the command is not 'pwd', it updates the current directory path based on the command. The function does not explicitly specify its functionality beyond this point.

