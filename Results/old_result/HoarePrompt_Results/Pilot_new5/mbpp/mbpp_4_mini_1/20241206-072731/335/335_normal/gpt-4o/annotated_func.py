#State of the program right berfore the function call: main_string is a string, and sub_string is a non-empty string.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None, indicating that there is no result to provide since 'sub_string' is not found in 'main_string'
    #State of the program after the if block has been executed: *`main_string` is a string, `sub_string` is a non-empty string, and `start_pos` is a valid index (0 or greater) representing the position of `sub_string` in `main_string`.
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #The program returns the non-empty string 'sub_string', the valid index 'start_pos', and 'end_pos' which is equal to 'start_pos + len(sub_string)'
#Overall this is what the function does:The function accepts a string `main_string` and a non-empty string `sub_string`, returning None if `sub_string` is not found in `main_string`. If found, it returns `sub_string`, the starting index of its first occurrence, and the ending index.

