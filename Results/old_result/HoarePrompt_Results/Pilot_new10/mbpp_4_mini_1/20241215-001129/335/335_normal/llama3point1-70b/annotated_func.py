#State of the program right berfore the function call: string is a non-empty string, and substring is a non-empty string that is shorter than or equal to string.
def func_1(string, substring):
    start = string.find(substring)
    if (start == -1) :
        return None
        #The program returns None, indicating that the substring was not found in the string.
    #State of the program after the if block has been executed: *`string` is a non-empty string, `substring` is a non-empty string that is shorter than or equal to `string`, and `start` is a non-negative integer representing the index of the first occurrence of `substring` in `string`.
    end = start + len(substring)
    return substring, start, end - 1
    #The program returns substring, the starting index start, and the ending index end - 1, where end is equal to start + len(substring)
#Overall this is what the function does:The function accepts a non-empty string and a non-empty substring and checks whether the substring exists within the string. If the substring is found, it returns the substring along with its starting index and ending index within the string. If the substring is not found, it returns None. There are no checks in place for the case where the substring is the same length as the string or if it appears multiple times; the function only reports the first occurrence.

