#State of the program right berfore the function call: tuples is a tuple of tuples, where all inner tuples have the same length and contain numbers.
def func_1(tuples):
    return [(sum(val) / len(tuples)) for val in zip(*tuples)]
    #The program returns a list of averages, where each average corresponds to the mean of the numbers in the same position across all inner tuples in `tuples`.
#Overall this is what the function does:The function accepts a tuple of tuples with numbers of the same length, and returns a list of averages where each average corresponds to the mean of the numbers in the same position across all inner tuples, but it may raise exceptions for invalid inputs such as empty tuples, non-numeric values, or tuples of different lengths.

