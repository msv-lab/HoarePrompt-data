#State of the program right berfore the function call: main_string and sub_string are strings.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: `main_string` is a string, `sub_string` is a string, `start_pos` is the position of the first occurrence of `sub_string` in `main_string` and is not equal to -1, meaning `sub_string` is found in `main_string`.
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #The program returns sub_string which is a string, start_pos which is the position of the first occurrence of sub_string in main_string, and end_pos which is start_pos plus the length of sub_string
#Overall this is what the function does:The function `func_1` accepts two string parameters, `main_string` and `sub_string`, and returns either `None` or a tuple containing `sub_string`, its start position, and its end position within `main_string`. If `sub_string` is found in `main_string`, the function returns a tuple with the `sub_string`, its start position (the index of the first character of `sub_string` in `main_string`), and its end position (the index after the last character of `sub_string` in `main_string`). If `sub_string` is not found in `main_string`, the function returns `None`. The function effectively locates the first occurrence of `sub_string` within `main_string` and provides the details of this occurrence, or indicates that no occurrence was found. The function does not modify either of the input strings.

