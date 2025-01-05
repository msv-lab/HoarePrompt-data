#State of the program right berfore the function call: a and b are integers such that 1 ≤ a, b ≤ 1000.
def func_1():
    trips = []
    for i in range(1, 1001):
        for j in range(1, 1001):
            k = (i ** 2 + j ** 2) ** 0.5
            if k.is_integer():
                k = int(k)
                trips.append([i, j, k])
        
    #State of the program after the  for loop has been executed: `a` and `b` are integers such that 1 ≤ `a` ≤ 1000 and 1 ≤ `b` ≤ 1000; `trips` contains all valid integer triplets `[i, j, k]` where k is calculated as the integer value of the square root of the sum of the squares of `i` and `j` for all `i, j` from 1 to 1000.
    a, b = get_list()
    for (i, j, k) in trips:
        if a % k == 0 and b % k == 0:
            mul1 = a // k
            mul2 = b // k
            if i * mul1 != mul2 * j:
                func_2('YES')
                func_2(0, 0)
                func_2(j * mul1, i * mul1)
                func_2(-i * mul2, j * mul2)
                return
        
    #State of the program after the  for loop has been executed: `a` and `b` are assigned values from `get_list()`, `trips` contains all the trips processed. If for any trip both `a` and `b` are divisible by `k` and `i * (a // k)` is not equal to `(b // k) * j`, the function would have returned, otherwise no return occurs. If no trip satisfies the divisibility condition, no operations are performed, and the variables remain unchanged.
    func_2('NO')
#Overall this is what the function does:The function generates all integer triplets (i, j, k) such that k is the integer value of the square root of the sum of squares of i and j, for all integers i and j from 1 to 1000. It then retrieves two integers a and b from a function `get_list()`. For each triplet, if both a and b are divisible by k and the condition i * (a // k) is not equal to (b // k) * j holds true, it calls another function `func_2()` with specific arguments and returns immediately. If none of the triplets satisfy the condition, it calls `func_2('NO')`. The function does not have explicit parameters and can return with no explicit value or return results from the `func_2()` calls.

#State of the program right berfore the function call: a and b are integers such that 1 ≤ a, b ≤ 1000.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `a` is an integer such that 1 ≤ `a` ≤ 1000, `b` is an integer such that 1 ≤ `b` ≤ 1000, `sep` is either a value from `kwargs` or a space, `file` is either a value from `kwargs` or `sys.stdout`, `at_start` is False, and the values of all elements in `args` have been written to `file`, separated by `sep` if there is more than one element in `args`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`a` is an integer such that 1 ≤ `a` ≤ 1000, `b` is an integer such that 1 ≤ `b` ≤ 1000, `sep` is either a value from `kwargs` or a space, `file` is either a value from `kwargs` or `sys.stdout`, `at_start` is False, and the value associated with `'end'` has been written to `file`. If the value of `kwargs.pop('flush', False)` is True, the output buffer of `file` has been flushed.
#Overall this is what the function does:The function accepts no parameters and prints the values of `args` to a specified output stream. The values are separated by a specified separator `sep`, which defaults to a space. The function also allows for an optional ending string `end` to be added after printing the values, defaulting to a newline. If the flush option is set to True, it flushes the output buffer of the file. However, the function does not handle any input for `args`, `kwargs`, or error handling, which may lead to issues if not properly provided during execution. Additionally, as the function does not return any value, its return type is implicitly `None`.

