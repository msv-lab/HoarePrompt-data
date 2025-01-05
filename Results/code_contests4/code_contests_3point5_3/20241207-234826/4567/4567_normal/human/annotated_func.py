#State of the program right berfore the function call: a and b are integers such that 1 ≤ a, b ≤ 1000.**
def func_1():
    trips = []
    for i in range(1, 1001):
        for j in range(1, 1001):
            k = (i ** 2 + j ** 2) ** 0.5
            if k.is_integer():
                k = int(k)
                trips.append([i, j, k])
        
    #State of the program after the  for loop has been executed: Output State: `a` is 1000, `b` is 1000, `k` is an integer, `trips` contains all possible Pythagorean triplets [i, j, k] where i, j, and k are integers. If no triplets are found, trips remains an empty list.
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
        
    #State of the program after the  for loop has been executed: `a` is 1000, `b` is 1000, `k` is an integer, trips contains all possible Pythagorean triplets, `mul1` is the floor division result of `a` divided by `k`, `mul2` is the floor division result of `b` divided by `k`. If `a % k == 0` and `b % k == 0`, and for all triplets in trips, `i * mul1` is equal to `mul2 * j`, then no specific value is returned.
    func_2('NO')
#Overall this is what the function does:The function iterates over all possible Pythagorean triplets within the given range of integers. It then checks specific conditions involving the variables `a`, `b`, `i`, `j`, and `k`. If the conditions are met, it calls func_2 with different arguments but does not return any specific value.

#State of the program right berfore the function call: a and b are integers such that 1 ≤ a, b ≤ 1000.**
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: 'a' and 'b' are integers such that 1 ≤ a, b ≤ 1000, 'sep' is ' ', 'file' is sys.stdout, `at_start` is False, 'args' has been completely iterated over and all elements have been written to the file.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *'a' and 'b' are integers such that 1 ≤ a, b ≤ 1000, 'sep' is ' ', 'file' is sys.stdout, `at_start` is False, 'args' has been completely iterated over and all elements have been written to the file. The file now contains a newline character at the end. The 'flush' key has been popped from 'kwargs' and its value is True if present.
#Overall this is what the function does:The function `func_2` does not accept any parameters but relies on the constraints that the integers `a` and `b` should be such that 1 ≤ a, b ≤ 1000. It processes the `kwargs` dictionary to handle printing values to a stream or `sys.stdout`. The function iterates over the elements in `args`, writing them to the file with the specified separator. It then writes the specified end character to the file and flushes the file if the 'flush' key is present in `kwargs` with a value of True. The function does not explicitly return any output but performs printing operations based on the provided constraints.

