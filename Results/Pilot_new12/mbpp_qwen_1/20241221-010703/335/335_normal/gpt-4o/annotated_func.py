#State of the program right berfore the function call: main_string is a string and sub_string is a non-empty string.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: Postcondition: `main_string` is a string, `sub_string` is a non-empty string, `start_pos` is the starting position of `sub_string` in `main_string`, and `start_pos` is not equal to -1
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #`The program returns sub_string, start_pos, and end_pos where sub_string is a non-empty string, start_pos is the starting position of sub_string in main_string, and end_pos is equal to start_pos + len(sub_string)`
#Overall this is what the function does:- The code currently does not handle the case where `main_string` is an empty string. To cover this, we should add a check at the beginning of the function to return `None` if `main_string` is empty.

