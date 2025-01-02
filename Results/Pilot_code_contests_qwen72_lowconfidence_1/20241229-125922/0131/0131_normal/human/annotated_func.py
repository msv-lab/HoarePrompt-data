#State of the program right berfore the function call: t is a positive integer representing the number of test cases, n is a positive integer representing the number of participants in each test case, and the input for each test case includes a line with n space-separated integers representing the number of problems solved by each participant in non-increasing order.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        g, s, b = 0, 0, 0
        
        l = 0
        
        p = -1
        
        for i, j in enumerate(map(int, input().split())):
            if i > n // 2:
                break
            if p != j:
                if g == 0:
                    g = l
                elif s <= g:
                    s += l
                else:
                    b += l
                l = 0
            l += 1
            p = j
        
        if g == 0 or s == 0 or b == 0 or g >= s or g >= b:
            func_2(0, 0, 0)
        else:
            func_2(g, s, b)
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer, `_` is in the range [0, t-1], `n` is a positive integer representing the number of participants in each test case, `g` is the length of the longest sequence of consecutive identical integers encountered up to the midpoint of the input for the last test case, `s` is the sum of the lengths of sequences of consecutive identical integers where the length is less than or equal to `g` for the last test case, `b` is the sum of the lengths of sequences of consecutive identical integers where the length is greater than `g` for the last test case, `l` is 0, `p` is the last integer processed (up to the midpoint) for the last test case, `i` is the index of the last integer processed (up to the midpoint) for the last test case, `j` is the last integer processed for the last test case. If `g == 0` or `s == 0` or `b == 0` or `g >= s` or `g >= b` for any test case, `func_2(0, 0, 0)` is called, otherwise `func_2(g, s, b)` is called with the respective values of `g`, `s`, and `b` for the last test case.
#Overall this is what the function does:The function does not handle invalid input (e.g., non-integer inputs or negative numbers).
-

#State of the program right berfore the function call: args is a tuple containing any number of arguments of any type, and kwargs is a dictionary that can contain the keys 'sep', 'file', 'end', and 'flush'. 'sep' is a string used to separate the arguments when printed, 'file' is a stream object to which the output will be written, 'end' is a string appended after the last value, and 'flush' is a boolean indicating whether to forcibly flush the stream.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` is a tuple containing any number of arguments of any type, `kwargs` is a dictionary that can contain the keys 'end' and 'flush', `sep` is a string equal to the value of 'sep' from `kwargs` or ' ' if 'sep' was not in `kwargs`, `file` is a stream object equal to the value of 'file' from `kwargs` or `sys.stdout` if 'file' was not in `kwargs`, `at_start` is `False` if `args` is not empty, otherwise `at_start` remains `True`. The string representations of all elements in `args` have been written to `file`, separated by `sep` if there are multiple elements.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is a tuple containing any number of arguments of any type, `kwargs` is a dictionary that may or may not contain the key 'flush' but does not contain the key 'end', `sep` is a string equal to the value of 'sep' from `kwargs` or ' ' if 'sep' was not in `kwargs`, `file` is a stream object equal to the value of 'file' from `kwargs` or `sys.stdout` if 'file' was not in `kwargs`, `at_start` is `False` if `args` is not empty, otherwise `at_start` remains `True`. If 'flush' is present in `kwargs`, it is removed, and `file` is flushed. Otherwise, `kwargs` remains unchanged and `file` is not flushed.
#Overall this is what the function does:The function `func_2` prints a series of values to a specified stream (defaulting to `sys.stdout`), separating them with a specified separator (defaulting to a space), and appending a specified end character (defaulting to a newline). It also optionally flushes the stream if the `flush` keyword argument is set to `True`. The function modifies the `kwargs` dictionary by removing the keys `'sep'`, `'file'`, and `'end'` during its execution. If `'flush'` is present and `True`, it is also removed after flushing the stream. The function does not return any value. Potential edge cases include: if `args` is empty, nothing is written to the stream except the `end` character; if `file` is not writable, an error may occur; if `flush` is `True` but the stream does not support flushing, an error may occur.

