#State of the program right berfore the function call: main_string is a string and sub_string is a non-empty string.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None, indicating that no specific value or variable has been found.
    #State of the program after the if block has been executed: *`main_string` is a string, `sub_string` is a non-empty string, and `start_pos` is a non-negative integer indicating the position where `sub_string` is found in `main_string` (not -1).
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #The program returns sub_string which is a non-empty string, start_pos which is a non-negative integer, and end_pos which is equal to start_pos + len(sub_string)
#Overall this is what the function does:The function accepts a string `main_string` and a non-empty string `sub_string`. It returns `None` if `sub_string` is not found in `main_string`. If `sub_string` is found, it returns `sub_string`, along with the start and end positions of `sub_string` within `main_string`. The end position is calculated as the start position plus the length of `sub_string`.

