#State of the program right berfore the function call: n and k are integers such that 1 ≤ n, k ≤ 10^{14}.
def func_1():
    arr = list(map(int, raw_input().strip().split(' ')))
    return arr
    #The program returns the list of integers 'arr' from the input
#Overall this is what the function does:The function accepts no parameters and returns a list of integers parsed from the input. It reads a line of input, splits it by spaces, converts each split segment to an integer, and stores them in a list. There are no checks for input validity or handling for empty input, which could lead to an error if the input is not as expected.

