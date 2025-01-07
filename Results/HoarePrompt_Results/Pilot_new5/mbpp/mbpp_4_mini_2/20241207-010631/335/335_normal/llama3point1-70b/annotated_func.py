#State of the program right berfore the function call: string is a non-empty string, and substring is a non-empty string.
def func_1(string, substring):
    start = string.find(substring)
    if (start == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: *`string` is a non-empty string, `substring` is a non-empty string, `start` is a non-negative integer (i.e., `start` is greater than or equal to 0)
    end = start + len(substring)
    return substring, start, end - 1
    #The program returns the 'substring', the 'start' index, and the 'end - 1' index, where 'end' is equal to 'start + len(substring)'
#Overall this is what the function does:The function accepts two non-empty strings, `string` and `substring`. It checks if `substring` exists within `string`. If `substring` is not found, it returns None. If found, it returns a tuple containing `substring`, the starting index of `substring` in `string`, and the ending index of `substring` (inclusive).

