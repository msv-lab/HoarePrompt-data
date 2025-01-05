#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^14.
def func_1():
    arr = list(map(int, raw_input().strip().split(' ')))
    return arr
    #The program returns the list of integers contained in 'arr' derived from the input
#Overall this is what the function does:The function accepts no parameters and returns a list of integers derived from user input, where the input is read from standard input as a space-separated string of integers. It does not handle any potential input errors, such as invalid input formats or empty input strings.

