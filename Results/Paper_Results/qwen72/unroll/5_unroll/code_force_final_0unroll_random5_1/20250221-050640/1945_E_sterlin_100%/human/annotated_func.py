#State of the program right berfore the function call: None
def func_1():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value input by the user. After the function concludes, the program has returned an integer value that was provided by the user.

#State of the program right berfore the function call: None.
def func_2():
    return map(int, input().split())
    #The program returns an iterator that will convert each element of the input string, split by spaces, into an integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an iterator that converts each element of an input string, split by spaces, into an integer. The input string is read from the standard input (e.g., user input or a redirected file). After the function concludes, the program state is unchanged except for the returned iterator, which can be used to access the converted integers.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_3` does not take any parameters. It simply reads input from the user and returns it as a list of integers.
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers entered by the user, where each integer is separated by a space.
#Overall this is what the function does:The function `func_3` reads a line of input from the user, where the input is expected to be a sequence of integers separated by spaces. It then converts this sequence into a list of integers and returns this list. The function does not modify any external state or variables.

#State of the program right berfore the function call: None
def func_4():
    return input()
    #The program returns the input provided by the user.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns the input provided by the user. After the function concludes, the program state includes the user input as the return value.

#State of the program right berfore the function call: This function does not take any parameters, and it is used to read input from the user, which is expected to be a string that can be split into multiple parts.
def func_5():
    return input().split()
    #The program returns a list of strings, where each string is a part of the input provided by the user, split by whitespace.
#Overall this is what the function does:The function `func_5` reads a line of input from the user and returns a list of strings, where each string is a part of the input split by whitespace. The function does not take any parameters. After the function concludes, the program state includes the returned list of strings, which can be used for further processing.

