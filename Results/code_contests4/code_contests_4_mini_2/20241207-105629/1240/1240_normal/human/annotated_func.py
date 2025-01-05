#State of the program right berfore the function call: The input path is a non-empty string consisting of lowercase Latin letters and the character '/', with at least one leading '/' and a maximum length of 100 characters.
def func_1():
    count = 0
    flag = 0
    while True:
        a = sys.stdin.read(1)
        
        if a == '/':
            if flag == 0:
                flag = 1
            else:
                pass
        elif a == '\n':
            break
        else:
            if flag == 1:
                sys.stdout.write('/')
            count += 1
            sys.stdout.write(a)
            flag = 0
        
    #State of the program after the loop has been executed: `count` is the total number of non-newline characters read before encountering a newline, `flag` is 0, as the loop terminates upon reading a newline character.
    if (not count) :
        sys.stdout.write('/')
    #State of the program after the if block has been executed: *`count` is the total number of non-newline characters read before encountering a newline, `flag` is 0. If `count` is 0, `sys.stdout.write('/')` outputs a forward slash and the value of `count` remains 0.
#Overall this is what the function does:The function reads characters from standard input until a newline is encountered. It writes each character to standard output while counting the total number of non-newline characters read. If it encounters a '/' character, it checks a flag to determine if it should write a '/' or not, effectively skipping consecutive slashes. If no non-newline characters are read, it outputs a single '/'. The function does not accept any parameters and does not return any value.

