#State of the program right berfore the function call: n is a positive integer representing the number of commands. Each command parameter is a non-empty string containing only lowercase Latin letters, slashes, and dots. The length of each command parameter is between 1 and 200 characters inclusive.**
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
        
    #State of the program after the  for loop has been executed: `cur` is a list containing the final elements after processing all the input values, `i` is the total number of iterations the loop executed, and `s` is a string. If `s` is equal to 'pwd', `cur` remains an empty list and `i` remains 0. If `s` is not equal to 'pwd', then `cur` contains the processed elements after each iteration, `i` is a non-negative integer representing the total number of iterations, and `s` is split at space index 1. If `s[0]` is '/', then `cur` will be an empty list and `s[0]` will be equal to the character at index 2 to the end of the original string.
#Overall this is what the function does:The function `func` does not accept any parameters. It processes a positive integer `n` representing the number of commands. Each command parameter is a non-empty string containing only lowercase Latin letters, slashes, and dots, with a length between 1 and 200 characters inclusive. The function then iterates through the commands where if the command is 'pwd', it prints the current path. If the command is not 'pwd', it manipulates the current path based on the command. The function updates the `cur` list to reflect the current path structure after processing all commands.

