#State of the program right berfore the function call: **
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = [int(x) for x in input().split()]
        
        func_2(Counter(a).most_common()[0][1])
        
    #State of the program after the  for loop has been executed: `t` is greater than 0, `n` is an input integer, `a` is a list of integers created from user input. The most common frequency in the list `a` is passed to `func_2` for each iteration of the loop.
#Overall this is what the function does:The function func_1 reads an integer t as input, then for each iteration in the range of t, it reads an integer n followed by a list of integers a. It then finds the most common frequency in the list a and calls func_2 with that frequency as an argument. The function does not accept any parameters and does not return any value.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the number of balls. a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ n and a_i ≤ a_{i+1} for all 1 ≤ i < n.**
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `sep` can be any value, `file` is determined by the 'file' key in `kwargs` or `sys.stdout`, `at_start` is False, `args` has at least 1 element, and all elements in `args` have been written to the file.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *After the execution of the if-else block, `sep` can have any value, `file` is determined by the 'file' key in `kwargs` or `sys.stdout`, `at_start` is False, `args` has at least 1 element, and all elements in `args` have been written to the file. Additionally, the value popped from `kwargs` with the key 'end' is written to the file using the `write` method if the 'flush' key was popped from `kwargs`, otherwise no changes occur.
#Overall this is what the function does:The function `func_2` does not explicitly accept any parameters. It processes multiple test cases, each defined by a positive integer `t` representing the number of test cases, and a positive integer `n` representing the number of balls in each test case. The function iterates through the sequence of integers `a_1, a_2, ..., a_n` for each test case to determine the arrangement of balls. There is no explicit return value from the function, but it is likely that the function performs operations or calculations to achieve the desired ball arrangement for each test case. The function writes the processed data to a specified file stream or `sys.stdout` based on the provided constraints. However, there is missing functionality in the annotations regarding how the ball arrangement is determined and the specific operations performed within the function.

