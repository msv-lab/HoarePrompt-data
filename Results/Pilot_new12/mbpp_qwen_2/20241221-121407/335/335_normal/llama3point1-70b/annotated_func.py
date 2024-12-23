#State of the program right berfore the function call: string is a string, and substring is also a string.
def func_1(string, substring):
    start = string.find(substring)
    if (start == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: `string` is a string, `substring` is a string, `start` is an index of the first occurrence of `substring` in `string`, or -1 if `substring` is not found in `string`. The condition `start != -1` is false.
    end = start + len(substring)
    return substring, start, end - 1
    #`substring`, start which is -1, end - 1 which is len(substring) - 2
#Overall this is what the function does:The function `func_1` accepts two parameters: `string` and `substring`, both of which are strings. It searches for the first occurrence of `substring` within `string`. If `substring` is found, it returns `substring` along with the `start` and `end` indices of its first occurrence. If `substring` is not found, it returns `None`. 

- In Case_1, if `substring` is not found in `string`, the function returns `None`.
- In Case_2, if `substring` is found in `string`, the function returns `substring`, the `start` index of the first occurrence of `substring` (which is `-1` when not found), and the `end` index (which is `len(substring) - 2` when not found).

Thus, the function aims to locate a substring within a given string and provide the substring along with its starting and ending indices if found, or return `None` if the substring is not present.

