#State of the program right berfore the function call: N is an integer such that 2 <= N <= 100000, and A is a list of N integers where each A[i] is in the range 1 <= A[i] <= 1000000000.
def func_1():
    n = int(input())
    a = sorted(readlist())
    gcd_arr = [0] * (n + 1)
    for i in range(n):
        gcd_arr[i + 1] = gcd(gcd_arr[i], a[i])
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 2 <= `N` <= 100000; `A` is a sorted list of `N` integers; `gcd_arr[1]` is equal to `A[0]`; `gcd_arr[i]` contains the GCD of the first `i` elements of `A` for `1 <= i <= n`; `gcd_arr[n]` is the GCD of all elements in `A[0]` to `A[n-1]`, and `i` is `n-1`.
    gcd_arr_rev = [0] * (n + 1)
    for i in reversed(range(n)):
        gcd_arr_rev[i] = gcd(gcd_arr_rev[i + 1], a[i])
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 2 <= `N` <= 100000; `A` is a sorted list of `N` integers; `gcd_arr[1]` is equal to `A[0]`; `gcd_arr[i]` contains the GCD of the first `i` elements of `A`; `gcd_arr[n]` is the GCD of all elements in `A[0]` to `A[n-1]`; `gcd_arr_rev[0]` is the GCD of all elements in `A`; for all `i` in range `1` to `n`, `gcd_arr_rev[i]` is the GCD of `A[i]` to `A[N-1]`.
    res = 0
    for i in range(n):
        res = max(res, gcd(gcd_arr[i], gcd_arr_rev[i + 1]))
        
    #State of the program after the  for loop has been executed: `res` is the maximum GCD of any prefix and any suffix (excluding an empty set) of the sorted list `A`.
    func_2(res)
#Overall this is what the function does:The function accepts an integer `N` (where 2 <= N <= 100000) and a list `A` of `N` integers (each between 1 and 1,000,000,000). It calculates the maximum GCD of any prefix and any suffix of the sorted list `A`, excluding empty sets. The final result is then passed to another function `func_2()`.

#State of the program right berfore the function call: N is an integer such that 2 <= N <= 100000, and A_i are integers such that 1 <= A_i <= 1000000000 for i from 1 to N.
def func_2():
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `at_start` is False; `file` has written the string representations of all elements in `args` separated by `sep`.
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`at_start` is False; `file` has been modified to include either the value of `kwargs['end']` or `b'\n'; if `kwargs` has the key `flush` with a value of True, then `file` is flushed, otherwise, `file` remains unchanged.
#Overall this is what the function does:The function accepts a variable number of positional arguments (`args`) and keyword arguments (`kwargs`). It writes the string representations of the positional arguments to a specified output stream (`file`), separated by a specified separator (`sep`). After writing the arguments, it appends an ending string (`end`) to the output. If the `flush` keyword argument is set to True, it flushes the output stream. The function does not return any value.

