#State of the program right berfore the function call: None
def func_1():
    return [int(x) for x in stdin.readline().split()]
    #The program returns a list of integers converted from the input string split by spaces. The input string is read from `stdin`.
#Overall this is what the function does:The function `func_1` reads a single line of input from standard input (`stdin`), splits the input string by spaces, converts each resulting substring into an integer, and returns a list of these integers. If the input contains non-integer values, a `ValueError` will be raised. If the input is empty or only contains whitespace, the function will return an empty list.

#State of the program right berfore the function call: None
def func_2():
    return int(stdin.readline())
    #The program returns an integer read from the standard input.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer from the standard input and returns it. If the input cannot be converted to an integer (e.g., if the user inputs a non-numeric value), a `ValueError` will be raised. The function does not handle any input validation or errors, so it is the responsibility of the caller to ensure that the input is valid. After the function completes, the program state is unchanged except for the returned integer value.

#State of the program right berfore the function call: None. This function does not take any parameters.
def func_3():
    return stdin.readline().strip()
    #The program returns the input string read from the standard input (stdin), with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_3` reads a line of input from the standard input (stdin), removes any leading and trailing whitespace from the input, and returns the resulting string. If no input is provided or the input is entirely whitespace, the function will return an empty string.

