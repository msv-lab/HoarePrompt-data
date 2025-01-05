#State of the program right berfore the function call: **
def func_1():
    n, k = get_list()
    li = get_list()
    req = set()
    for i in li:
        r = 0
        
        while i > 0:
            j = 0
            while i % k ** (j + 1) == 0:
                j += 1
            i //= k ** j
            j += r
            if j in req:
                func_2('NO')
                return
            req.add(j)
            r = j
            i -= 1
        
    #State of the program after the  for loop has been executed: 'req' is a set containing all unique values of 'j' after all iterations, 'r' is the final value of 'j', 'li' is a non-empty list, 'i' is 0, 'k' is defined, 'j' is the final value after all iterations, 'i' is updated through floor division with 'k' raised to the power of 'j', all final values of 'j' after all iterations are in 'req'
    func_2('YES')
#Overall this is what the function does:The function `func_1` processes a list of integers by performing operations involving variables 'n', 'k', 'li', 'req', 'r', 'i', and 'j' within nested loops. It updates 'req' with unique values of 'j', checks if certain conditions are met, and may call another function `func_2` with different arguments based on those conditions. The function has multiple potential return cases based on different scenarios involving the variables and sets mentioned, but it does not accept any parameters.

#State of the program right berfore the function call: **Precondition**: 
- n is an integer such that 1 ≤ n ≤ 30.
- k is an integer such that 2 ≤ k ≤ 100.
- a is a list of n integers where each element is in the range [0, 10^16].
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `at_start` is False, `args` is not empty, `x` is the last element in `args`, `file.write(sep)` is executed, `file.write(str(x))` is executed
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`at_start` is False, `args` is not empty, `x` is the last element in `args`, `file.write(sep)` is executed, `file.write(str(x))` is executed, `kwargs.pop('end', '\n')` is executed. If `flush` key is True and popped from `kwargs`, then the program state remains unchanged.
#Overall this is what the function does:The function `func_2` does not accept any parameters explicitly but works with predefined parameters `n`, `k`, and `a`. It iterates through the elements in `args`, printing each element to a stream defined by `file`. The function handles the printing of elements with specified separators and end characters. If the `flush` key is True in the provided `kwargs`, it flushes the stream. However, it lacks clarity on how `args` is defined and how the elements of `a` are related to the printing process. The annotations mention the existence of `args` but it is not explicitly defined in the function signature.

