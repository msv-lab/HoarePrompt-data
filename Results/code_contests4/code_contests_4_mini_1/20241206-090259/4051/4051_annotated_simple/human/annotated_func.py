#State of the program right berfore the function call: n and k are integers such that 1 ≤ n, k ≤ 10^14.
def func_1():
    arr = list(map(int, raw_input().strip().split(' ')))
    return arr
    #The program returns the list of integers 'arr' obtained from input
#Overall this is what the function does:The function does not accept any parameters and returns a list of integers obtained from user input. The input is read as a space-separated string, which is then converted into a list of integers. There are no validations for input constraints, so if the input is not valid integers or exceeds the expected format, it may result in an error. The function will return an empty list if no input is provided.

