#State of the program right berfore the function call: None
def func_1():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value that is input by the user. After the function concludes, the program state includes the returned integer, which is the user's input converted to an integer.

#State of the program right berfore the function call: No variables are passed to the function func_2. The function is expected to read input from the standard input, which should be a line of space-separated integers.
def func_2():
    return map(int, input().split())
    #The program returns an iterator that yields integers from the line of space-separated integers provided as input.
#Overall this is what the function does:The function `func_2` reads a line of space-separated integers from the standard input and returns an iterator that yields each integer from the input line.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers, where each integer is derived from the input provided by the user, split by spaces.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a line of input from the user, splits the input by spaces, converts each resulting string into an integer, and returns a list of these integers. The final state of the program after the function concludes is that it has a list of integers derived from the user's input.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_4` does not take any parameters.
def func_4():
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns the input provided by the user.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_5():
    return input().split()
    #The program returns a list of strings, where each string is a part of the input provided by the user, split by whitespace.
#Overall this is what the function does:The function `func_5` does not accept any parameters and returns a list of strings. Each string in the list is a part of the input provided by the user, split by whitespace. The function effectively captures user input and splits it into a list of substrings based on spaces or other whitespace characters.

