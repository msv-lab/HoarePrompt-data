#State of the program right berfore the function call: The input is a non-empty string representing a path that starts with at least one '/' character and contains only lowercase Latin letters and '/' characters, with a length of no more than 100 characters.
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
        
    #State of the program after the loop has been executed: `count` is the total number of non-newline characters read before a newline, `flag` is 0, and the loop terminates when a newline character is encountered.
    if (not count) :
        sys.stdout.write('/')
    #State of the program after the if block has been executed: *`count` is the total number of non-newline characters read before a newline, and `flag` is 0. If `count` equals 0, then a '/' is written to standard output. There is no else part to consider in this scenario.
#Overall this is what the function does:The function reads characters from standard input one at a time until it encounters a newline character. It counts the number of non-newline characters read. If it encounters a '/' character, it ensures that only one '/' is printed in sequence, regardless of how many are read consecutively. If no non-newline characters are read before the newline, it outputs a single '/'. The function does not accept any parameters and primarily interacts with standard input and output.

