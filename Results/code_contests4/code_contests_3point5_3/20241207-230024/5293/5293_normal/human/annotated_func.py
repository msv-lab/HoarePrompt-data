#State of the program right berfore the function call: **
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = [int(x) for x in input().split()]
        
        func_2(Counter(a).most_common()[0][1])
        
    #State of the program after the  for loop has been executed: List `a` is created based on the user input values for each iteration, `n` is an input integer, and the value returned by func_2 after each iteration
#Overall this is what the function does:The function `func_1` reads an integer `t` from input, then iterates `t` times. Within each iteration, it reads an integer `n` and a list of integers `a`. It then calls another function `func_2` with the count of the most common element in list `a`. The function does not accept any parameters, and its purpose is to handle user input for `n` and `a`, and pass relevant information to `func_2`.

#State of the program right berfore the function call: **
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: If `at_start` is False, `args` is an iterable with at least one element, `x` is the last element in `args` and `at_start` is False. Otherwise, if `at_start` is True, `args` is an empty iterable and `at_start` is True.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *If `at_start` is False, then after executing the if block, `args` is an iterable with at least one element where `x` is the last element, `at_start` remains False, and `flush` is removed from `kwargs`. If `at_start` is True, after executing the if block, `args` is an empty iterable, `at_start` remains True, and `flush` is removed from `kwargs`.
#Overall this is what the function does:The function func_2 does not accept any parameters and iterates over the elements in `args`, writing them to a file specified in `kwargs` or `sys.stdout` by default. It handles the `sep`, `end`, and `flush` keyword arguments in the `kwargs` dictionary. If `flush` is True, it flushes the file. However, the annotations mention the removal of `sep` and `end` from `kwargs` but do not show the actual code for this action. Thus, the functionality does not align with the annotations in handling these cases.

