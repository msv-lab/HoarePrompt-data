#State of the program right berfore the function call: string is a non-empty string and substring is a non-empty string.
def func_1(string, substring):
    start = string.find(substring)
    if (start == -1) :
        return None
        #The program returns None, indicating that no value is returned from the function.
    #State of the program after the if block has been executed: *`string` is a non-empty string, `substring` is a non-empty string, and `start` is an integer representing the index of `substring` in `string`, which is greater than or equal to 0.
    end = start + len(substring)
    return substring, start, end - 1
    #The program returns the substring, the index of the substring in the string, and the end index minus one, where the substring is a non-empty string, start is an integer index greater than or equal to 0, and end is equal to start plus the length of the substring.
#Overall this is what the function does:The function accepts two non-empty strings, `string` and `substring`. It returns None if `substring` is not found within `string`. If `substring` is found, it returns the `substring`, the starting index of `substring` in `string`, and the ending index of the substring within `string`. The function does not handle cases where `substring` appears multiple times in `string`; it only returns the first occurrence.

