#State of the program right berfore the function call: No variables are present in the function signature of `func_1`. This function is expected to read input from standard input and return a map object containing integers, which presumably represent the values of `n` and `x` or elements of the permutation `p` in the context of the problem.
def func_1():
    return map(int, input().split())
    #The program returns a map object containing integers that were read from standard input and split by whitespace.
#Overall this is what the function does:The function `func_1` reads a line of input from standard input, splits it into components based on whitespace, converts each component to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: This function does not have any parameters, and thus no precondition can be specified based on the function signature alone.
def func_2():
    return list(func_1())
    #The program returns the list returned by `func_1()`
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns the list returned by `func_1()`.

