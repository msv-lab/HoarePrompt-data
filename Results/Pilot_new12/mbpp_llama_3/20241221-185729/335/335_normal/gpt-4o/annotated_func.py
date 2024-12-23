#State of the program right berfore the function call: main_string and sub_string are strings.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: `main_string` is a string, `sub_string` is a string, `start_pos` is the starting position of `sub_string` in `main_string` and `start_pos` is not equal to -1, meaning `sub_string` is found in `main_string`
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #The program returns a string 'sub_string', the starting position 'start_pos' of 'sub_string' in 'main_string' where 'start_pos' is not equal to -1, and the ending position 'end_pos' which is 'start_pos' plus the length of 'sub_string'.
#Overall this is what the function does:The function `func_1` accepts two string parameters, `main_string` and `sub_string`. It searches for the first occurrence of `sub_string` within `main_string`. If `sub_string` is found, it returns a tuple containing the `sub_string`, its starting position (`start_pos`), and its ending position (`end_pos`) within `main_string`. If `sub_string` is not found in `main_string`, it returns `None`. The function does not modify the input strings and does not handle any potential exceptions that may occur during execution, such as `main_string` or `sub_string` being `None` or not being strings. The function's return values indicate whether the search was successful and, if so, provide information about the location of `sub_string` within `main_string`.

