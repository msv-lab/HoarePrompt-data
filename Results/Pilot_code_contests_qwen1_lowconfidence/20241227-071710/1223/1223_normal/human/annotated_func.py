#State of the program right berfore the function call: s is a 4-character string consisting of uppercase English letters.
def func_1():
    s = Counter(input()).values()
    func_2('Yes' if s == [2, 2] else 'No')
#Overall this is what the function does:The function `func_1` takes no parameters and processes a 4-character string `s` consisting of uppercase English letters. It counts the occurrences of each character in `s`, storing these counts in a list `s`. It then calls `func_2` with either 'Yes' or 'No', depending on whether the counts are exactly two occurrences of two different characters (i.e., the list `s` is equal to `[2, 2]`). If the counts do not match this condition, `func_2` is called with 'No'. An edge case is when `s` does not have exactly four characters, which would cause `Counter(input())` to raise an error if `input()` is not properly constrained. Additionally, the function does not handle the case where `s` contains duplicate characters other than the two required, which would still result in `s == [2, 2]` being true.

#State of the program right berfore the function call: S is a string consisting of exactly 4 uppercase English letters.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `S` is a string consisting of exactly 4 uppercase English letters, `sep` is the value passed in `kwargs` if provided, else ' ', `file` is the value passed in `kwargs` if provided, else `sys.stdout`, `at_start` is `False`, and the string representations of all elements in `args` have been written to `file` with each element preceded by `sep` except the first one.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`S` is a string consisting of exactly 4 uppercase English letters, `sep` is the value passed in `kwargs` if provided, else ' ', `file` is the value passed in `kwargs` if provided, else `sys.stdout`, `at_start` is `False`, and the end value written to `file` is `kwargs.pop('end', '\n')`. If `kwargs.pop('flush', False)` is `True`, file buffers are flushed.
#Overall this is what the function does:The function `func_2` takes a variable number of arguments `args`, and keyword arguments `kwargs`. It writes the string representations of these arguments to a specified output stream (`file`), separated by a specified separator (`sep`), and ends with a specified end character. If `flush` is set to `True`, it flushes the output buffer. The function does not return anything. After executing, the `file` stream will contain the concatenated string representations of the arguments with the specified separator and end character, and the `sep`, `file`, and `end` values from `kwargs` will be reflected in the final state. If no `sep` or `end` is provided, default values (' ' and '\n') are used respectively.

