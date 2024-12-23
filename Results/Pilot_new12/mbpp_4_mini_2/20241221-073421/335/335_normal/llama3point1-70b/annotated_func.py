#State of the program right berfore the function call: string is a non-empty string, and substring is a non-empty string.
def func_1(string, substring):
    start = string.find(substring)
    if (start == -1) :
        return None
        #The program returns None, indicating that the operation does not produce a result.
    #State of the program after the if block has been executed: *`string` is a non-empty string, `substring` is a non-empty string, `start` is the index of the first occurrence of `substring` in `string`, and `start` is greater than or equal to 0.
    end = start + len(substring)
    return substring, start, end - 1
    #The program returns the substring along with the start index of its first occurrence and the end index (which is end - 1) where the substring appears in the string. The start index is greater than or equal to 0, and end is equal to start + len(substring).
#Overall this is what the function does:The function accepts two non-empty strings, `string` and `substring`. It first searches for the first occurrence of `substring` in `string`. If `substring` is not found, the function returns `None`. If `substring` is found, the function returns a tuple consisting of `substring`, the start index of its first occurrence, and the end index (exclusive) calculated as the start index plus the length of `substring`. The start index is guaranteed to be zero or greater if `substring` exists in `string`. However, the function does not handle cases where `string` or `substring` are empty, nor does it handle multiple occurrences of `substring`, as it always returns the first occurrence found, if any.

