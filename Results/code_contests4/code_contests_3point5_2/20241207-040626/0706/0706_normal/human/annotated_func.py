#State of the program right berfore the function call: **
def func_1():
    return map(long, stdin.readline().split())
    #The program returns a map object containing the long integers parsed from the input read from stdin
#Overall this is what the function does:The function `func_1` reads input from stdin, parses the input into long integers, and returns a map object containing these long integers. The function does not accept any parameters. If the input cannot be parsed into long integers, it may result in a ValueError.

#State of the program right berfore the function call: **
def func_2(li):
    if (not li) :
        return
        #The program returns an empty list after entering the if condition (not li)
    #State of the program after the if block has been executed: *`li` is a list. The list `li` is not empty
    for i in xrange(len(li) - 1):
        stdout.write('%d ' % li[i])
        
    #State of the program after the  for loop has been executed: `li` is a list with at least 2 elements, and all elements in `li` except the last one are printed
    stdout.write('%d\n' % li[-1])
#Overall this is what the function does:The function func_2 accepts a list li and prints all elements of the list except the last one with a space after each element and a newline character after the last element. If the input list is empty, the function returns without printing anything.

#State of the program right berfore the function call: **
def func_3():
    return stdin.readline().rstrip()
    #The program returns the input string read from the standard input without any trailing whitespace
#Overall this is what the function does:The function func_3 reads an input string from the standard input and returns it without any trailing whitespace. It does not handle any errors or exceptions that might occur during the input reading process.

