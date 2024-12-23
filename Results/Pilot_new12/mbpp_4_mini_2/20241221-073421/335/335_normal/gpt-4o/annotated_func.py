#State of the program right berfore the function call: main_string is a string, sub_string is a string, and sub_string is not an empty string.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None, indicating that there is no relevant value to return as 'sub_string' was not found in 'main_string'
    #State of the program after the if block has been executed: *`main_string` is a string, `sub_string` is a string, `sub_string` is not an empty string, `start_pos` is the index of the first occurrence of `sub_string` in `main_string`, and `start_pos` is greater than or equal to 0.
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #The program returns sub_string, start_pos (the index of the first occurrence of sub_string in main_string), and end_pos (which is start_pos plus the length of sub_string)
#Overall this is what the function does:The function `func_1` accepts two string parameters: `main_string` and `sub_string` (where `sub_string` is guaranteed to be non-empty). It searches for the first occurrence of `sub_string` within `main_string`. If `sub_string` is not found, it returns None. If it is found, the function returns a tuple containing `sub_string`, the start index of its first occurrence (`start_pos`), and the end index of that occurrence (`end_pos`, which is calculated as `start_pos` plus the length of `sub_string`). The function does not handle cases where `main_string` or `sub_string` may be None, nor does it address scenarios where either parameter is not a string. Overall, it provides information about the location of `sub_string` within `main_string`, or indicates its absence.

