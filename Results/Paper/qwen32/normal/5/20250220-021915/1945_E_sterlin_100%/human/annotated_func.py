#State of the program right berfore the function call: No variables are present in the function signature.
def func_1():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value that is input by the user.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. The function is expected to read input from standard input, which consists of integers separated by spaces, and return a map object that applies the `int` function to each item in the input split by spaces.
def func_2():
    return map(int, input().split())
    #The program returns a map object that applies the `int` function to each item in the input split by spaces.
#Overall this is what the function does:The function `func_2` reads a line of input from standard input, which is expected to be a string of integers separated by spaces, and returns a map object that applies the `int` function to each of these integers, converting them into a sequence of integers.

#State of the program right berfore the function call: The function `func_3` does not take any parameters and returns a list of integers. The integers in the list are obtained by splitting the input string, which is expected to contain space-separated integers.
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained by splitting the input string, which is expected to contain space-separated integers.
#Overall this is what the function does:The function `func_3` reads a line of input from the user, splits it into substrings based on spaces, converts each substring into an integer, and returns a list of these integers.

#State of the program right berfore the function call: The function `func_4` does not take any parameters and returns the result of the `input()` function, which is a string representing the user's input.
def func_4():
    return input()
    #The program returns the string that the user inputs.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns a string that the user inputs.

#State of the program right berfore the function call: The function `func_5` does not take any parameters and returns a list of strings, which are the space-separated values read from the input.
def func_5():
    return input().split()
    #The program returns a list of strings that are the space-separated values read from the input.
#Overall this is what the function does:The function `func_5` reads a line of input from the user, splits it into space-separated values, and returns these values as a list of strings.

