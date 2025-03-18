#State of the program right berfore the function call: No variables are present in the function signature of `func_1`. This function is expected to read input from the standard input, split it into integers, and return them as a map object.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains integers parsed from the input string, where the input string is split by whitespace.
#Overall this is what the function does:The function `func_1` reads a line of input from the standard input, splits it into substrings based on whitespace, converts each substring into an integer, and returns these integers as a map object.

#State of the program right berfore the function call: No variables are present in the function signature provided. The function `func_2` does not have any parameters.
def func_2():
    return list(func_1())
    #The program returns a list derived from the return value of `func_1()`
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list derived from the return value of `func_1()`.

