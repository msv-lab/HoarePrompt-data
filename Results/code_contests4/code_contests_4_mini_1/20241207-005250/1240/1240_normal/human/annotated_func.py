#State of the program right berfore the function call: The input is a non-empty string representing a path that starts with at least one character '/', contains only lowercase Latin letters and '/' characters, and has a length of no more than 100 characters.
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
        
    #State of the program after the loop has been executed: `count` is the total number of non-newline characters read from standard input before encountering a newline character, `flag` is 0, indicating that the last character read was not '/', and the loop has exited after reading a newline character.
    if (not count) :
        sys.stdout.write('/')
    #State of the program after the if block has been executed: *If `count` is 0, `flag` is 0, and '/' is written to standard output. There are no other cases since there is no else part in the code.
#Overall this is what the function does:The function reads characters from standard input until it encounters a newline character. It writes each character to standard output, inserting a '/' before each character after the first '/' encountered. If no characters are read before the newline, it writes a single '/'. The function does not accept any parameters and does not return a value.

