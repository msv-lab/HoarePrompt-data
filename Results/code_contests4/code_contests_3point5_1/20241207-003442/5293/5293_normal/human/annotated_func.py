#State of the program right berfore the function call: **t is a positive integer, n is a positive integer, and a_i (for 1 ≤ i ≤ n) are positive integers such that a_i ≤ a_{i+1} for all 1 ≤ i < n.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = [int(x) for x in input().split()]
        
        func_2(Counter(a).most_common()[0][1])
        
    #State of the program after the  for loop has been executed: t is a positive integer, n is the last input integer, a_i (for 1 ≤ i ≤ n) are positive integers such that a_i ≤ a_{i+1} for all 1 ≤ i < n, a is a list containing the last input integers, and func_2() is called with the frequency of the most common element in list a
#Overall this is what the function does:The function `func_1` reads an integer `t` from input, then for each iteration in the range of `t`, it reads an integer `n`, a list of integers `a`, and calls another function `func_2` with the frequency of the most common element in list `a`. The function does not accept any parameters and does not return any value.

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
        
    #State of the program after the  for loop has been executed: `sep` is either the popped value or ' ', `file` is either the popped value or `sys.stdout`, `at_start` is False, `args` has at least 1 element, all elements in `args` have been written to the `file` using `file.write()` function with `sep` in between each element.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`sep` is either the popped value or ' ', `file` is either the popped value or `sys.stdout`, `at_start` is False, `args` has at least 1 element, all elements in `args` have been written to the `file` using `file.write()` function with `sep` in between each element, the value popped from `kwargs` using 'end' key is written to the `file` with a newline character by `file.write()`. If kwargs.pop('flush', False) is True, then the file is flushed.
#Overall this is what the function does:The function func_2 does not accept any parameters and does not return any value. It processes the elements in args by writing them to a file specified in kwargs or sys.stdout with a separator specified in kwargs. It then writes the value specified by the 'end' key in kwargs to the file with a newline character. If the 'flush' key in kwargs is True, the file is flushed.

