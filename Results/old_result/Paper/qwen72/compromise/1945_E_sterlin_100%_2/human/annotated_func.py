#State of the program right berfore the function call: None
def func_1():
    return int(input())
    #The program returns an integer value provided by the user.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value provided by the user. After the function concludes, the program state includes the returned integer, which is the result of the user's input.

#State of the program right berfore the function call: None. This function does not take any parameters and is used to read input from the user, converting it into integers.
def func_2():
    return map(int, input().split())
    #The program returns a map object that converts user input into integers, where the user input is expected to be a series of numbers separated by spaces.
#Overall this is what the function does:The function `func_2` reads a line of user input, expecting a series of numbers separated by spaces, and returns a map object that converts these numbers into integers. The function does not take any parameters and does not modify any external state. After the function concludes, the user input has been processed and is available as a map object of integers.

#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by converting the input string, which is split by spaces, into integers.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a line of input from the user, splits the input string by spaces, converts each resulting substring into an integer, and returns a list of these integers. The function affects the program by consuming user input and producing a list of integers.

#State of the program right berfore the function call: None
def func_4():
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns the input provided by the user. After the function concludes, the program state includes the user's input as the return value.

#State of the program right berfore the function call: None. This function does not take any parameters and is used to read input, which is not directly related to the variables in the problem description.
def func_5():
    return input().split()
    #The program returns a list of strings, where each string is a part of the user input split by whitespace.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It reads a line of user input and returns a list of strings, where each string is a part of the input split by whitespace. The function does not modify any external variables or state.

