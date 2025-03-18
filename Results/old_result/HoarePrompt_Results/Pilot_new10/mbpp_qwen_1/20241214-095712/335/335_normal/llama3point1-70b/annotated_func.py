#State of the program right berfore the function call: string is a string and substring is a non-empty string.
def func_1(string, substring):
    start = string.find(substring)
    if (start == -1) :
        return None
        #`The program returns None`
    #State of the program after the if block has been executed: `string` is a string, `substring` is a non-empty string, `start` is the index of the first occurrence of `substring` in `string` if it exists, otherwise -1, and `start` is not equal to -1
    end = start + len(substring)
    return substring, start, end - 1
    #`substring` as originally defined, `start` as the index of the first occurrence of `substring` in `string`, and `end - 1` which is `start + len(substring) - 1`
#Overall this is what the function does:The function `func_1` accepts two parameters: `string` (a string) and `substring` (a non-empty string). It returns `None` if `substring` is not found in `string`. If `substring` is found, it returns a tuple containing the starting index of the first occurrence of `substring` in `string` and the ending index (`end - 1`), which is `start + len(substring) - 1`.

