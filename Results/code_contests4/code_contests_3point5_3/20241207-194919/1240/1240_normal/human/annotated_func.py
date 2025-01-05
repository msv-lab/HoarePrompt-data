#State of the program right berfore the function call: The input path is a string containing lowercase Latin letters and character '/', starting with at least one character '/'. The length of the path is no more than 100 characters and is not empty.**
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
        
    #State of the program after the loop has been executed: The loop will continue indefinitely, reading input characters one at a time. If the character is '/', the flag will be set to 1. If the character is '\n', the loop will break. If the character is neither '/' nor '\n', the count will be updated and the character will be output. After the loop finishes, 'count' holds the total count of characters that were not '/' and were not part of the newline character. 'flag' will be 0.
    if (not count) :
        sys.stdout.write('/')
    #State of the program after the if block has been executed: *The loop reads input characters indefinitely. If the character is '/', the flag is set to 1. If the character is '\n', the loop breaks. If the character is neither '/' nor '\n', the count is updated and the character is output. After the loop finishes, 'count' holds the total count of characters that were not '/' and were not part of the newline character. If count is 0, '/' is written to the standard output. 'flag' is set to 1 if '/' was encountered during the loop, otherwise 'flag' remains 0.
#Overall this is what the function does:The function `func_1` reads input characters indefinitely. If the character is '/', the flag is set to 1. If the character is '\n', the loop breaks. If the character is neither '/' nor '\n', the count is updated, and the character is output. After the loop finishes, 'count' holds the total count of characters that were not '/' and were not part of the newline character. If count is 0, '/' is written to the standard output. 'flag' is set to 1 if '/' was encountered during the loop; otherwise, 'flag' remains 0.

