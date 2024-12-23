#State of the program right berfore the function call: main_string and sub_string are strings.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: `main_string` is a string, `sub_string` is a string, `start_pos` is the index where `sub_string` starts in `main_string`, and `start_pos` is not equal to -1
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #The program returns sub_string which is a string, start_pos which is the index where sub_string starts in main_string and is not equal to -1, and end_pos which is start_pos + len(sub_string)
#Overall this is what the function does:The function `func_1` accepts two parameters: `main_string` and `sub_string`, both of which are strings. It searches for `sub_string` within `main_string`. If `sub_string` is found, the function returns `sub_string`, the starting index (`start_pos`) of `sub_string` in `main_string`, and the ending index (`end_pos`) of `sub_string` in `main_string`. If `sub_string` is not found, the function returns `None`. This covers all potential cases where `sub_string` may or may not be present in `main_string`.

