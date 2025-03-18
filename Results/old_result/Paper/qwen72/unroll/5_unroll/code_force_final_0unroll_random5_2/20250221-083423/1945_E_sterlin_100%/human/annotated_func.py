#State of the program right berfore the function call: None. This function does not take any parameters and is used to read an integer input, likely representing the number of test cases t.
def func_1():
    return int(input())
    #The program returns an integer value that is input by the user, likely representing the number of test cases.
#Overall this is what the function does:The function `func_1` reads an integer value from the user input and returns this integer value. The function does not take any parameters. After the function concludes, the program has an integer value that was provided by the user, which is typically used to represent the number of test cases.

#State of the program right berfore the function call: None. The function `func_2` does not take any parameters and is used to read input, which is not directly related to the variables in the main problem's function signature.
def func_2():
    return map(int, input().split())
    #The program returns a map object that converts each element of the input (split by spaces) into an integer.
#Overall this is what the function does:The function `func_2` reads a string of numbers separated by spaces from the user, converts each number into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are passed to the function, and it is expected to read input from stdin.
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers that were input by the user, separated by spaces.
#Overall this is what the function does:The function `func_3` reads a line of input from the standard input (stdin), splits the input by spaces, converts each split part into an integer, and returns a list of these integers. The function does not modify any external state or variables. After the function concludes, the user will have a list of integers that were provided as input.

#State of the program right berfore the function call: None
def func_4():
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns the input provided by the user. After the function concludes, the program state includes the user's input as the return value.

#State of the program right berfore the function call: None. The function `func_5` does not take any parameters and is used to read input, which is not directly related to the problem's main variables.
def func_5():
    return input().split()
    #The program returns a list of strings, where each string is a part of the input provided by the user, split by whitespace.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It reads a line of input from the user and returns a list of strings, where each string is a part of the input split by whitespace.

