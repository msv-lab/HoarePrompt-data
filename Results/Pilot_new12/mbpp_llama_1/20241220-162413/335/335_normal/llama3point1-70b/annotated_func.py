#State of the program right berfore the function call: string and substring are strings.
def func_1(string, substring):
    start = string.find(substring)
    if (start == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: `string` is a string, `substring` is a string, `start` is the index of the first occurrence of `substring` in `string`, and `start` is not equal to -1, meaning `substring` is found in `string`
    end = start + len(substring)
    return substring, start, end - 1
    #The program returns substring that is a string, the index of the first occurrence of substring in string, and the index of the last character of the first occurrence of substring in string
#Overall this is what the function does:The function takes two string parameters, `string` and `substring`, and returns either `None` if `substring` is not found in `string`, or a tuple containing the `substring`, the index of its first occurrence in `string`, and the index of its last character in `string`. The function performs a search operation to find the first occurrence of `substring` in `string`, and if found, it calculates and returns the start and end indices of the match. The function handles edge cases where `substring` is not present in `string` by returning `None`, but it does not handle cases where `string` or `substring` are empty strings, which may be considered edge cases depending on the context in which the function is used. Additionally, the function does not account for overlapping matches or multiple occurrences of `substring` in `string`, it only reports the first occurrence. The state of the input variables `string` and `substring` remains unchanged after the function execution.

