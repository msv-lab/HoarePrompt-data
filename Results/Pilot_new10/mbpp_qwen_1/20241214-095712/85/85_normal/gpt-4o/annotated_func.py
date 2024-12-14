#State of the program right berfore the function call: arr is a list of integers.
def func_1(arr):
    min_val = min(arr)
    max_val = max(arr)
    max_diff = max_val - min_val
    return max_diff
    #The program returns max_val - min_val, where max_val is the maximum value in list 'arr' and min_val is the minimum value in list 'arr'
#Overall this is what the function does:The function accepts a list of integers `arr` and returns the difference between the maximum and minimum values in the list.

