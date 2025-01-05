#State of the program right berfore the function call: The input path is a string containing lowercase Latin letters and character '/', starting with at least one character '/'. The length of the string is no more than 100 characters and it is not empty.**
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
        
    #State of the program after the loop has been executed: The input path is a string containing lowercase Latin letters and character '/', starting with at least one character '/'. If 'a' is '/', then flag is 1. If 'a' is not equal to '\n', count is the number of characters in the input path excluding the leading '/', flag is 0. If flag is 1, the program remains in the same state and the letter 'a' is printed to the standard output. If 'a' is '\n', the flag remains 0.
    if (not count) :
        sys.stdout.write('/')
    #State of the program after the if block has been executed: *The input path is a string containing lowercase Latin letters and character '/', starting with at least one character '/'. If 'a' is '/', then flag is 1. If 'a' is not equal to '\n', count is the number of characters in the input path excluding the leading '/', flag is 0. If flag is 1, the program remains in the same state and the letter 'a' is printed to the standard output. If 'a' is '\n', the flag remains 0. The count is equal to 0.
#Overall this is what the function does:The function `func_1` reads input characters from the standard input until it encounters a newline character. It processes the input path, which is a string containing lowercase Latin letters and '/', with a special handling for the '/' character. If the count of characters in the input path is 0, it prints '/' to the standard output. This function does not accept any parameters and does not return any value.

