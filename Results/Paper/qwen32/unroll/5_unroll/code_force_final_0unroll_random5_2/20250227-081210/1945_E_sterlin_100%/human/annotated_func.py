#State of the program right berfore the function call: No variables in the function signature. The function `func_1` does not take any parameters and is expected to return an integer.
def func_1():
    return int(input())
    #The program returns an integer that is input by the user.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer that is input by the user.

#State of the program right berfore the function call: The function `func_2` does not have any parameters. It returns a map object which is an iterator of integers obtained by splitting the input string and converting each split string into an integer.
def func_2():
    return map(int, input().split())
    #The program returns a map object which is an iterator of integers obtained by splitting the input string and converting each split string into an integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an input string, splits it into components, converts each component into an integer, and returns a map object which is an iterator of these integers.

#State of the program right berfore the function call: The function `func_3` does not take any parameters and returns a list of integers. The integers in the list are obtained by splitting a line of input, which is expected to contain space-separated values representing the input for a test case.
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by splitting a line of input, which is expected to contain space-separated values representing the input for a test case.
#Overall this is what the function does:The function `func_3` reads a line of input from the user, splits it into space-separated values, converts each value to an integer, and returns a list of these integers.

#State of the program right berfore the function call: This function does not take any parameters and returns the result of the input() function, which is a string.
def func_4():
    return input()
    #The program returns the string input by the user.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns the string input by the user.

#State of the program right berfore the function call: No variables are present in the function signature of `func_5()`.
def func_5():
    return input().split()
    #The program returns a list of strings, where each string is a substring from the input provided by the user, split by whitespace.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It prompts the user for input, splits the input string by whitespace, and returns a list of the resulting substrings.

