#State of the program right berfore the function call: main_string is a string and sub_string is a non-empty string.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: Postcondition: `main_string` is a string, `sub_string` is a non-empty string, `start_pos` is the lowest index where `sub_string` is found in `main_string`.
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #`main_string` is a string, `sub_string` is a non-empty string, `start_pos` is the lowest index where `sub_string` is found in `main_string`, `end_pos` is the value of `start_pos + len(sub_string)`, `sub_string` is the substring found at `start_pos` in `main_string`
#Overall this is what the function does:The function accepts a string `main_string` and a non-empty string `sub_string`. It returns `None` if `sub_string` is not found in `main_string`, otherwise it returns a tuple containing the found substring, its starting position, and its ending position in `main_string`.

