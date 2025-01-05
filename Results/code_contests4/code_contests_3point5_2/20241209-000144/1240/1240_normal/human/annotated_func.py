#State of the program right berfore the function call: The input is a string representing a path to a directory, starting with at least one '/'. The length of the string is no more than 100 characters.**
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
        
    #State of the program after the loop has been executed: 'count' is the total number of characters read from sys.stdin except for the newline character, 'flag' is 0, 'a' is the last character read before encountering a newline character
    if (not count) :
        sys.stdout.write('/')
    #State of the program after the if block has been executed: *'count' is the total number of characters read from sys.stdin except for the newline character, 'flag' is 0, 'a' is the last character read before encountering a newline character. If the count is not equal to 0, the program retains the initial state. Otherwise, the program does not change as there is no else part.
#Overall this is what the function does:The function `func_1` reads characters from the standard input until a newline character is encountered. It validates the input string representing a path to a directory by ensuring it starts with at least one '/' and has a maximum length of 100 characters. If the count of characters read is not zero, it outputs the characters read, and if it is zero, it outputs a single '/'. The function does not explicitly return any value but serves as a validator for the path string input.

