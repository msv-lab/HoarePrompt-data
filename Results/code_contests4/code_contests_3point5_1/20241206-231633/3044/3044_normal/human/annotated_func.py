#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50. Each command parameter is a non-empty string containing lower case Latin letters, slashes, and dots.**
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
        
    #State of the program after the  for loop has been executed: `cur` is a list containing the final elements after processing all the input strings, `i` is the integer value after the last iteration, `s` is an empty string
#Overall this is what the function does:The function `func` reads input strings and processes them to simulate a simplified version of a command-line interface. It maintains a current directory `cur` as a list of directory names. If the input string is 'pwd', it prints the current directory path. If the input string is a command to change the directory, it updates the current directory accordingly. The function does not accept any parameters, and the final state includes the list `cur` containing the elements after processing all input strings, the integer `i` after the last iteration, and an empty string `s`. The annotations mention constraints on the input parameters, but these constraints are not enforced or utilized in the actual code.

