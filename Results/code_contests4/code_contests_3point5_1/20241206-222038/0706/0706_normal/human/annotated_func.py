#State of the program right berfore the function call: **
def func_1():
    return map(long, stdin.readline().split())
    #The program returns a map object created by applying the function 'long' to each element in the input read from the standard input.
#Overall this is what the function does:The function func_1 reads input from standard input, splits the input, converts each element to a long integer, and returns a map object containing these converted long integers.

#State of the program right berfore the function call: n is a positive integer, xi are integers such that 2 <= xi <= 10^7, m is a positive integer, and li, ri are integers such that 2 <= li <= ri <= 2*10^9.**
def func_2(li):
    if (not li) :
        return
        #The program does not return any value
    #State of the program after the if block has been executed: *n is a positive integer, xi are integers such that 2 <= xi <= 10^7, m is a positive integer, and li, ri are integers such that 2 <= li <= ri <= 2*10^9. The value of li is non-zero
    for i in xrange(len(li) - 1):
        stdout.write('%d ' % li[i])
        
    #State of the program after the  for loop has been executed: n is a positive integer, each xi is an integer such that 2 <= xi <= 10^7, m is a positive integer, li is a list with a length of at least 2, ri is an integer such that 2 <= li <= ri <= 2*10^9, and the value of li is non-zero
    stdout.write('%d\n' % li[-1])
#Overall this is what the function does:The function `func_2` accepts a list `li` as a parameter and prints each element of the list followed by a space except for the last element which is followed by a newline character. The function does not return any value. It operates under the assumption that `li` is a list with at least two elements.

#State of the program right berfore the function call: - n is an integer such that 1 <= n <= 10^6.
def func_3():
    return stdin.readline().rstrip()
    #The program returns the input read from stdin after removing any trailing whitespaces
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads input from stdin and returns the input after removing any trailing whitespaces. The input read from stdin is assumed to be an integer `n` such that 1 <= n <= 10^6.

