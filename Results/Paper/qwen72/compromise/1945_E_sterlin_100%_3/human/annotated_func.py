#State of the program right berfore the function call: None
def func_1():
    return int(input())
    #The program returns an integer value that the user inputs.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value that the user inputs. After the function concludes, the program state includes the returned integer value, which is the result of converting the user's input to an integer.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_2():
    return map(int, input().split())
    #The program returns a map object that converts each element of the input string, split by spaces, into an integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a map object that converts each element of an input string, split by spaces, into an integer. The input string is provided by the user through the `input()` function. After the function call, the program state includes a map object that can be iterated over to access the converted integers.

#State of the program right berfore the function call: None
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers created from the input provided by the user, where the input is split by spaces.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns a list of integers derived from user input, where the input is split by spaces. The function reads a line of input from the user, splits it into substrings based on spaces, converts each substring to an integer, and returns the resulting list. The state of the program after the function concludes is that it has a list of integers that were provided by the user.

#State of the program right berfore the function call: None
def func_4():
    return input()
    #The program returns the user input.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns the user input.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_5():
    return input().split()
    #The program returns a list of strings, where each string is a part of the input provided by the user, split by whitespace.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It reads a line of input from the user and returns a list of strings, where each string is a part of the input split by whitespace. The function does not modify any external variables or state. After the function concludes, the program has a list of strings derived from the user's input.

