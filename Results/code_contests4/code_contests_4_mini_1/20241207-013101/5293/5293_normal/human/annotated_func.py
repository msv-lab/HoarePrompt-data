#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, for each test case n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where 1 ≤ a_i ≤ n and the sequence is non-decreasing (a_1 ≤ a_2 ≤ ... ≤ a_n).
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = [int(x) for x in input().split()]
        
        func_2(Counter(a).most_common()[0][1])
        
    #State of the program after the  for loop has been executed: `t` is an integer such that 1 ≤ `t` ≤ 100; `n` is an input integer from the last iteration; `a` is a list of integers from the last iteration; `func_2` has been called `t` times with the frequency of the most common integer from each respective list `a`.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases, then for each test case, it accepts an integer `n` which indicates the length of a list. It reads a list `a` of `n` non-decreasing integers and calls another function `func_2` with the frequency of the most common integer in the list `a`. The function does not return any values or handle cases where the list might not contain any elements, assuming the input adheres to the specified constraints.

#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100) representing the number of test cases; for each test case, n is a positive integer (1 ≤ n ≤ 100), and a list of n integers a_1, a_2, …, a_n where each a_i (1 ≤ a_i ≤ n) is in non-decreasing order (a_1 ≤ a_2 ≤ … ≤ a_n).
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `t` is a positive integer (1 ≤ `t` ≤ 100), `n` is a positive integer (1 ≤ `n` ≤ 100), `args` is a non-empty iterable containing `n` elements; `file` contains the string representations of all elements in `args` separated by `sep`, `at_start` is False.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`t` is a positive integer (1 ≤ `t` ≤ 100), `n` is a positive integer (1 ≤ `n` ≤ 100), `args` is a non-empty iterable containing `n` elements; `file` contains the string representations of all elements in `args` separated by `sep`, `at_start` is False; the default value of `end` is '\n' is written to `file`. If the `flush` argument is evaluated as True, the flush method is called on `file`, ensuring that all buffered output is written to the underlying stream.
#Overall this is what the function does:The function accepts a variable number of arguments (args) and keyword arguments (kwargs). It prints each element in args to the specified output file (defaulting to sys.stdout) with a specified separator (defaulting to a space) and an ending character (defaulting to a newline). However, the function does not handle the input parameters `t` and `n` directly; rather, it is designed to process any iterable provided in `args`, assuming the caller will manage the test cases and input format. There are no explicit validations for the number of test cases, the range of integers in args, or the order of elements. If the flush keyword argument is set to True, it flushes the output buffer.

