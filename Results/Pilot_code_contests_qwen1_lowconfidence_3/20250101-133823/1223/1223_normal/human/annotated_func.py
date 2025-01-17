#State of the program right berfore the function call: s is a 4-character string consisting of uppercase English letters.
def func_1():
    s = Counter(input()).values()
    func_2('Yes' if s == [2, 2] else 'No')
#Overall this is what the function does:The function `func_1` takes no explicit parameters and does not return anything. It first counts the occurrences of each character in a 4-character string `s` (consisting of uppercase English letters) and stores these counts in the variable `s`. Then, it calls the function `func_2` with either 'Yes' or 'No' based on whether the counts stored in `s` are exactly `[2, 2]`. If the counts are not `[2, 2]`, `func_2` is called with 'No'. If the counts are `[2, 2]`, `func_2` is called with 'Yes'.

#State of the program right berfore the function call: S is a string of length 4 consisting of uppercase English letters.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `S` is a string of length 4, `sep` and `file` are set based on `kwargs` or default values, `at_start` is `False`, `args` contains all elements that were passed to the loop.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`S` is a string of length 4, `at_start` is False, `args` contains all elements that were passed to the loop, `file` now contains the value of `kwargs.pop('end', '\n')`, and the output buffer of `file` is flushed because the value of `kwargs.pop('flush', False)` is True.
#Overall this is what the function does:The function `func_2` takes a variable number of positional arguments (`args`) and keyword arguments (`kwargs`). It constructs a string by iterating over the positional arguments, separating them with a specified separator (`sep`), and writes the resulting string to a specified output stream (`file`). If the `end` keyword argument is provided, it appends it to the end of the string before writing. If the `flush` keyword argument is set to `True`, it flushes the output buffer. The function does not return any value.

