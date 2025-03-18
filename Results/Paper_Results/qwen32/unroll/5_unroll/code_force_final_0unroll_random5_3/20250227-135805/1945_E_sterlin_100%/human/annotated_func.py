#State of the program right berfore the function call: This function does not take any parameters and returns an integer, which is the input from the user.
def func_1():
    return int(input())
    #The program returns an integer that is the input from the user.
#Overall this is what the function does:The function prompts the user for input, converts that input to an integer, and returns it.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. This function is expected to read from standard input and return a map object containing integers.
def func_2():
    return map(int, input().split())
    #The program returns a map object containing integers that were read from the standard input, split by whitespace.
#Overall this is what the function does:The function `func_2` reads a line of input from the standard input, splits it into substrings based on whitespace, converts each substring into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: No variables are present in the function signature. The function `func_3` does not take any parameters and returns a list of integers obtained by mapping the input split by spaces to integers.
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by mapping the input split by spaces to integers.
#Overall this is what the function does:The function `func_3` takes no input parameters and returns a list of integers. These integers are derived by splitting a space-separated input string and converting each split component into an integer.

#State of the program right berfore the function call: The function `func_4` does not have any parameters, implying it does not rely on any external input values for its operation.
def func_4():
    return input()
    #The program returns the value that is input by the user.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns a value input by the user.

#State of the program right berfore the function call: No specific variables are present in the function signature for `func_5`. This function is not directly related to the core logic of the problem but seems to be a utility function to read input.
def func_5():
    return input().split()
    #The program returns a list of strings that are the words from the input provided by the user.
#Overall this is what the function does:The function `func_5` accepts no parameters and returns a list of strings, where each string is a word from the input provided by the user.

