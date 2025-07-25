#State of the program right berfore the function call: main_string is a string, and sub_string is a non-empty string.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None, indicating that `sub_string` is not found in `main_string` as `start_pos` is -1.
    #State of the program after the if block has been executed: *`main_string` is a string, `sub_string` is a non-empty string, and `start_pos` is a valid index of `sub_string` in `main_string` (not -1).
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #The program returns the non-empty string 'sub_string', the valid index 'start_pos' of 'sub_string' in 'main_string', and 'end_pos' which is equal to 'start_pos' plus the length of 'sub_string'
#Overall this is what the function does:The function accepts a string `main_string` and a non-empty string `sub_string`. It attempts to find the first occurrence of `sub_string` in `main_string`. If `sub_string` is not found, it returns None. If found, it returns the `sub_string`, the starting index of `sub_string` in `main_string`, and the ending index of `sub_string` in `main_string`, calculated as the starting index plus the length of `sub_string`.

