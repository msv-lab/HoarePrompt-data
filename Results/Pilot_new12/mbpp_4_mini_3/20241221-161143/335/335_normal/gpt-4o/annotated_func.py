#State of the program right berfore the function call: main_string is a string, sub_string is a non-empty string.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None, indicating that no value is found or returned from the operation.
    #State of the program after the if block has been executed: *`main_string` is a string, `sub_string` is a non-empty string, `start_pos` is the index of the first occurrence of `sub_string` in `main_string`, and `start_pos` is greater than or equal to 0.
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #The program returns sub_string which is a non-empty string, start_pos which is an index greater than or equal to 0, and end_pos which is equal to start_pos + len(sub_string)
#Overall this is what the function does:The function `func_1` accepts two parameters: a string `main_string` and a non-empty string `sub_string`. It attempts to locate the first occurrence of `sub_string` within `main_string`. If `sub_string` is found, the function returns `sub_string`, the starting index of its first occurrence (`start_pos`), and the ending index (`end_pos`), which is calculated as the starting index plus the length of `sub_string`. If `sub_string` is not found, the function returns `None`. The function does not handle cases where `main_string` or `sub_string` are empty or if `sub_string` exceeds the length of `main_string`, potentially resulting in unexpected behavior. Furthermore, the function does not specify what should happen if the input types are incorrect (e.g., if a non-string is provided).

