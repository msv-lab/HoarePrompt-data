#State of the program right berfore the function call: string is a non-empty string, and substring is a non-empty string.
def func_1(string, substring):
    start = string.find(substring)
    if (start == -1) :
        return None
        #The program returns None since the return statement explicitly states None, and the state of 'start' indicates that 'substring' is not found in 'string'.
    #State of the program after the if block has been executed: *`string` is a non-empty string, `substring` is a non-empty string, and `start` is a non-negative integer representing the index of the first occurrence of `substring` in `string`.
    end = start + len(substring)
    return substring, start, end - 1
    #The program returns the substring, its start index which is a non-negative integer, and its end index which is equal to start + len(substring) - 1
#Overall this is what the function does:The function accepts two parameters: a non-empty string (`string`) and a non-empty substring (`substring`). It searches for the first occurrence of `substring` within `string`. If `substring` is not found, it returns `None`. If found, it returns the `substring`, the start index of its first occurrence (a non-negative integer), and the end index (calculated as start + length of the substring - 1). The function does not handle cases where `substring` is empty, which could lead to unexpected behavior, as it is assumed to be non-empty from the context. Additionally, there are no check for invalid input types, so passing non-string types would result in an AttributeError.

