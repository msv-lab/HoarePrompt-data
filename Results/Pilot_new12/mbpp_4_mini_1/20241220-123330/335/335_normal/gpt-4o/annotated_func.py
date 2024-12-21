#State of the program right berfore the function call: main_string is a string, and sub_string is a non-empty string.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None, indicating that the operation does not provide any value.
    #State of the program after the if block has been executed: *`main_string` is a string, `sub_string` is a non-empty string, `start_pos` is a non-negative integer (the index of the first occurrence of `sub_string` in `main_string`), which is not equal to -1.
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #The program returns 'sub_string', 'start_pos' which is a non-negative integer, and 'end_pos' which is equal to start_pos plus the length of 'sub_string'
#Overall this is what the function does:The function `func_1` takes two parameters: `main_string`, which is a string, and `sub_string`, which is a non-empty string. It searches for the first occurrence of `sub_string` within `main_string`. If `sub_string` is found, it returns a tuple containing `sub_string`, the starting index (`start_pos`) of its first occurrence, and the ending index (`end_pos`) which is calculated as `start_pos` plus the length of `sub_string`. If `sub_string` is not found in `main_string`, the function returns None. It is important to note that the function does not handle cases where `main_string` might be empty or where `sub_string` does not occur in it at all, returning None in those cases.

