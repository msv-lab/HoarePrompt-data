#State of the program right berfore the function call: string and substring are strings.
def func_1(string, substring):
    start = string.find(substring)
    if (start == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: `string` is a string, `substring` is a string, `start` is the index of the first occurrence of `substring` in `string`, and `start` is not equal to -1, meaning `substring` is found in `string`
    end = start + len(substring)
    return substring, start, end - 1
    #The program returns the substring found in the string, the starting index of this substring, and the index of the last character of the substring.
#Overall this is what the function does:The function accepts two string parameters, `string` and `substring`, and returns `None` if `substring` is not found in `string`. If `substring` is found, it returns a tuple containing the `substring`, its starting index in `string`, and the index of its last character in `string`. The function assumes inputs are strings and does not perform input validation, which may lead to unexpected behavior with non-string inputs. It handles empty strings by returning `None` for an empty `substring` in a non-empty `string`, and a tuple with an empty string, start index 0, and end index -1 if both inputs are empty strings.

