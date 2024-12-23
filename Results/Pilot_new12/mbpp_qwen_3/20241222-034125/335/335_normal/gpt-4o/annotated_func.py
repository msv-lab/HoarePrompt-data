#State of the program right berfore the function call: main_string and sub_string are strings.
def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if (start_pos == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: `main_string` is a string, `sub_string` is a string, `start_pos` is the index of the first occurrence of `sub_string` in `main_string`
    end_pos = start_pos + len(sub_string)
    return sub_string, start_pos, end_pos
    #`sub_string`, the index of the first occurrence of `sub_string` in `main_string`, and `end_pos` which is `start_pos + len(sub_string)`
#Overall this is what the function does:The function `func_1` accepts two parameters: `main_string` and `sub_string`, both of which are strings. The function searches for the first occurrence of `sub_string` within `main_string`.

- If `sub_string` is not found in `main_string`, the function returns `None`.
- If `sub_string` is found in `main_string`, the function returns a tuple containing three elements: `sub_string` itself, the index of the first occurrence of `sub_string` in `main_string`, and `end_pos`, which is calculated as `start_pos + len(sub_string)`, where `start_pos` is the index of the first character of `sub_string`.

This function effectively locates the specified substring within a larger string and provides information about its position and length if found, or indicates absence of the substring by returning `None` if not found.

