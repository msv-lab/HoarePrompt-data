#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the number of piranhas, and a is a list of n positive integers where each integer represents the size of a piranha in the aquarium.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        m = max(a)
        
        f = 0
        
        for i in range(n):
            if a[i] == m:
                if i - 1 >= 0 and a[i] > a[i - 1] or i + 1 < n and a[i] > a[i + 1]:
                    func_2(i + 1)
                    f = 1
                    break
        
        if f == 0:
            func_2(-1)
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer, `n` is the input integer representing the number of piranhas, `a` is a list of integers representing the sizes of the piranhas, `m` is the maximum value in `a`, `f` is 0, and `func_2` has been called with appropriate arguments based on the condition met during the loop iterations. If no condition is met, `func_2` is called with the argument `-1`.
#Overall this is what the function does:The function processes a specified number of test cases. For each test case, it reads an integer `n` representing the number of piranhas and a list `a` of `n` positive integers representing the sizes of the piranhas. It then finds the maximum size `m` of the piranhas in the list `a`. The function checks if any piranha of size `m` has a neighboring piranha of smaller size. If such a piranha is found, it calls `func_2` with the index of the piranha plus one; otherwise, it calls `func_2` with `-1`. After processing all test cases, the function ensures that `func_2` is called appropriately based on the conditions met during the loop iterations. Potential edge cases include when there are no piranhas of size `m` with a neighboring smaller piranha, or when the list `a` contains only one element.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the number of piranhas in the aquarium, and a is a list of n positive integers representing the sizes of the piranhas.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `at_start` is False, `args` is an empty list or has no elements left to iterate over, and every element in `args` has been written to the file as a string separated by `sep` if not the first element.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`at_start` is False, `args` is an empty list or has no elements left to iterate over, the file has been written with `'\n'`. If `kwargs.pop('flush', False)` is True, the file buffer is flushed. The value of `kwargs` has been modified by popping 'flush', and the current value of `flush` is either True or False.
#Overall this is what the function does:The function does not accept any explicit parameters and its behavior is controlled through keyword arguments. It processes input for `t` test cases, where for each test case, it accepts `n` as the number of piranhas and `a` as a list of sizes of the piranhas. However, the function does not perform any operations on these inputs. Instead, it constructs a string representation of the arguments passed in the form of `args` and writes it to a file (or `sys.stdout` by default), separated by the `sep` character. After writing the arguments, it appends a newline character (`'\n'`) unless otherwise specified. If the `flush` keyword argument is set to `True`, it flushes the file buffer.

