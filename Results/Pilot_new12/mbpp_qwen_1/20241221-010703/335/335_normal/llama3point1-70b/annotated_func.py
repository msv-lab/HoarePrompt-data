#State of the program right berfore the function call: string is a string and substring is a non-empty string.
def func_1(string, substring):
    start = string.find(substring)
    if (start == -1) :
        return None
        #The program returns None
    #State of the program after the if block has been executed: `string` is a string, `substring` is a non-empty string, `start` is the index of `substring` in `string` if `substring` is found, otherwise -1. The value of `start` is not -1
    end = start + len(substring)
    return substring, start, end - 1
    #`substring`, the non-empty string found in `string` at index `start`; `start`, the index of where `substring` begins in `string`; `end - 1`, the index right before the end of `substring` in `string`
#Overall this is what the function does:The function `func_1` accepts two parameters: `string` and `substring`. `string` is a string, and `substring` is a non-empty string. The function searches for `substring` within `string`. If `substring` is not found, the function returns `None`. If `substring` is found, the function returns a tuple containing the `substring`, the index of where `substring` begins in `string` (inclusive), and the index right before the end of `substring` in `string` (exclusive).

Potential edge cases include:
- If `substring` is not found in `string`, the function correctly returns `None`.
- If `substring` is found, the function returns the correct indices, ensuring that the second index is right before the end of `substring`.

The function ensures that if `substring` is present in `string`, it provides the substring along with its starting and ending indices (excluding the end index). If `substring` is not found, it gracefully returns `None`.

