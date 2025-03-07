#State of the program right berfore the function call: None
def func_1():
    return int(input())
    #The program returns an integer value entered by the user.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value entered by the user. After the function concludes, the program has obtained an integer input from the user and the function has returned this integer.

#State of the program right berfore the function call: No variables are passed to the function func_2. The function is expected to read input from the standard input, which should be a line of space-separated integers.
def func_2():
    return map(int, input().split())
    #The program returns a map object that is an iterator over the integers obtained from the space-separated line of input.
#Overall this is what the function does:Reads a line of space-separated integers from the standard input and returns a map object that is an iterator over these integers.

#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads input from the standard input, which is expected to be a space-separated string of integers.
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers, where each integer is derived from the space-separated string of integers provided as input.
#Overall this is what the function does:The function `func_3` reads a space-separated string of integers from the standard input and returns a list of integers, where each integer is derived from the input string. The function does not modify any external variables or state.

#State of the program right berfore the function call: None. The function `func_4` does not take any parameters and is used to read input, likely for processing test cases or other inputs in the context of the problem.
def func_4():
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function `func_4` reads a line of input from the user and returns it as a string. The function does not accept any parameters and has no side effects on other variables or the program state. After the function concludes, the program has the user's input available as the return value.

#State of the program right berfore the function call: None. This function does not take any parameters and is used to read input, which is not directly related to the variables in the problem's main function.
def func_5():
    return input().split()
    #The program returns a list of strings, where each string is a part of the input provided by the user, split by whitespace.
#Overall this is what the function does:The function `func_5` reads a line of user input and returns a list of strings, where each string is a part of the input split by whitespace. The function does not accept any parameters.

