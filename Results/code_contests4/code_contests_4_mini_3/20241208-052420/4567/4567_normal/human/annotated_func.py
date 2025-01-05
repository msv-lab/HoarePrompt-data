#State of the program right berfore the function call: a and b are integers such that 1 ≤ a, b ≤ 1000.
def func_1():
    trips = []
    for i in range(1, 1001):
        for j in range(1, 1001):
            k = (i ** 2 + j ** 2) ** 0.5
            if k.is_integer():
                k = int(k)
                trips.append([i, j, k])
        
    #State of the program after the  for loop has been executed: `a` is an integer such that 1 ≤ `a` ≤ 1000, `b` is an integer such that 1 ≤ `b` ≤ 1000, `trips` contains all valid triplets `[i, j, k]` where `k` is the integer hypotenuse corresponding to the integer values of `i` and `j` calculated from the Pythagorean theorem for each `i` and `j` from 1 to 1000.
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
        
    #State of the program after the  for loop has been executed: `a` and `b` are integers within the range of 1 to 1000. If the loop executes, it checks all valid triplets in `trips`. If for any triplet `[i, j, k]`, both `a % k == 0` and `b % k == 0`, and if `i * (a // k) != (b // k) * j`, the function `func_2` is invoked with specific parameters, and the loop terminates. If no such triplet satisfies the conditions, the loop completes without returning from `func_2`.
    func_2('NO')
#Overall this is what the function does:The function calculates all valid Pythagorean triplets (i, j, k) where k is the integer hypotenuse derived from the Pythagorean theorem for integers i and j ranging from 1 to 1000. It then checks if the given integers a and b (both in the range 1 to 1000) are divisible by k. If they are, and if the resulting multiplication factor leads to a specific condition, it calls another function `func_2` with specific parameters. If no triplet meets the criteria, it calls `func_2` with 'NO'. The function does not return any values directly but may lead to multiple calls to `func_2` with various parameters based on the conditions met.

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
        
    #State of the program after the  for loop has been executed: `a` and `b` are integers such that 1 ≤ `a` ≤ 1000 and 1 ≤ `b` ≤ 1000; `sep` is a space; `file` is `sys.stdout`; `at_start` is False; `args` is a list of elements with at least one element written to `file` in string representation, separated by `sep`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`a` and `b` are integers such that 1 ≤ `a` ≤ 1000 and 1 ≤ `b` ≤ 1000; `sep` is a space; `file` is `sys.stdout`; `at_start` is False; `args` is a list of elements with at least one element written to `file` in string representation, separated by `sep`; a newline character has been written to `file`. If the `flush` keyword argument has been popped from `kwargs` and it is True, the content of `file` is flushed.
#Overall this is what the function does:The function accepts keyword arguments (`kwargs`) that allow specifying `sep`, `file`, `end`, and `flush`. It prints the elements from `args` to the specified `file`, separated by `sep`, followed by `end`. If `flush` is set to True, it flushes the output stream. The function does not return any value. However, it is important to note that `args` must be defined elsewhere for the function to operate correctly, and the function currently does not handle the case where `args` is empty, which could lead to unexpected behavior.

