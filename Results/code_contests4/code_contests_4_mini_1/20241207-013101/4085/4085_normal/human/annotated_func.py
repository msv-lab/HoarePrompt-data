#State of the program right berfore the function call: N is an integer such that 2 <= N <= 10^5, and A is a list of N integers where each integer A_i satisfies 1 <= A_i <= 10^9.
def func_1():
    n = int(input())
    a = sorted(readlist())
    gcd_arr = [0] * (n + 1)
    for i in range(n):
        gcd_arr[i + 1] = gcd(gcd_arr[i], a[i])
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 2 <= N <= 10^5, `n` is at least 1, `a` is a sorted list from input, `gcd_arr` is a list of size `n + 1` where `gcd_arr[n]` is the GCD of all elements in `a`.
    gcd_arr_rev = [0] * (n + 1)
    for i in reversed(range(n)):
        gcd_arr_rev[i] = gcd(gcd_arr_rev[i + 1], a[i])
        
    #State of the program after the  for loop has been executed: `gcd_arr_rev[0]` is the GCD of all elements in `a`, `gcd_arr_rev[i]` is the GCD of elements `a[i-1]` to `a[n-1]` for `1 <= i <= n`, `N` is an integer such that 2 <= N <= 10^5, `n` is at least 1, `a` is a sorted list from input, `gcd_arr` is a list of size `n + 1` where `gcd_arr[n]` is the GCD of all elements in `a`.
    res = 0
    for i in range(n):
        res = max(res, gcd(gcd_arr[i], gcd_arr_rev[i + 1]))
        
    #State of the program after the  for loop has been executed: `res` is the maximum GCD of `gcd_arr[i]` and `gcd_arr_rev[i + 1]` for all valid indices `i` from 0 to `n-1`, `gcd_arr` is a list of size `n + 1` containing GCD values, `gcd_arr_rev` is a list of size `n + 1` containing GCD values, `n` is the total number of elements in `a`.
    func_2(res)
#Overall this is what the function does:The function accepts an integer `N` (where 2 <= N <= 10^5) and a list `A` of `N` integers (where 1 <= A[i] <= 10^9). It calculates the maximum GCD between elements of the list when one element is excluded. The GCD is computed using two auxiliary arrays that store GCD values from the start and the end of the list, respectively. Finally, it passes the result to another function `func_2`.

#State of the program right berfore the function call: N is an integer such that 2 <= N <= 100000, and A is a list of N integers where each integer A_i satisfies 1 <= A_i <= 10^9.
def func_2():
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 2 <= `N` <= 100000; `A` is a list of `N` integers where each integer `A_i` satisfies 1 <= `A_i` <= 10^9; `sep` is the value from `kwargs`; `file` contains all elements of `args` written as strings separated by `sep`; `at_start` is False; `args` can be empty or a non-empty iterable.
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`N` is an integer such that 2 <= `N` <= 100000; `A` is a list of `N` integers where each integer `A_i` satisfies 1 <= `A_i` <= 10^9; `sep` is the value from `kwargs`; `file` has written the value of `kwargs.pop('end', b'\n')`; `at_start` is False; `args` can be empty or a non-empty iterable; if the value of `kwargs.pop('flush', False)` is True, then we flush the file.
#Overall this is what the function does:The function accepts a variable number of arguments and optional keyword arguments for formatting output. It writes each argument as a string to a specified output file, separating them with a specified separator, and appends an optional end character. If the flush keyword argument is set to True, it flushes the output file. The function does not explicitly handle the case where no arguments are provided, which could lead to no output being written to the file. Additionally, the function does not utilize the parameters N and A mentioned in the annotations, making those annotations misleading.

