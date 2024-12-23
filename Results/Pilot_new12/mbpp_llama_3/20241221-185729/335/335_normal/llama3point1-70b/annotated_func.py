#State of the program right berfore the function call: string and substring are strings.
def func_1(string, substring):
    start = string.find(substring)
    if (start == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: `string` is a string, `substring` is a string, `start` is the index of the first occurrence of `substring` in `string`, and `start` is not equal to -1, meaning `substring` is found in `string`
    end = start + len(substring)
    return substring, start, end - 1
    #The program returns the substring that is part of the string, the start index of this substring in the string, and the index of the last character of the substring in the string
#Overall this is what the function does:The function `func_1` accepts two string parameters, `string` and `substring`, and returns either `None` or a tuple containing the `substring`, its start index within the `string`, and the index of its last character. If the `substring` is found in the `string`, the function returns the `substring` along with its start and end indices. If the `substring` is not found in the `string`, the function returns `None`. The function handles cases where the `substring` is an empty string or the `string` itself, and it correctly calculates the end index of the `substring` as the start index plus the length of the `substring` minus one. The function does not handle cases where the input parameters are not strings, and it does not perform any error checking or handling for such cases. The function also does not modify the input strings in any way.

