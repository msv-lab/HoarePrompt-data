#State of the program right berfore the function call: main_string and sub_string are strings.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: `main_string` is a string, `sub_string` is a string, `start_pos` is the index of the first occurrence of `sub_string` in `main_string` and `start_pos` is not equal to -1, meaning `sub_string` is found in `main_string`
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #The program returns a string 'sub_string', an integer 'start_pos' that is the index of the first occurrence of 'sub_string' in 'main_string', and an integer 'end_pos' that is 'start_pos' plus the length of 'sub_string'
#Overall this is what the function does:The function accepts two strings, `main_string` and `sub_string`, and returns `None` if `sub_string` is not found in `main_string`; otherwise, it returns a tuple containing `sub_string`, its starting position, and its ending position in `main_string`.

