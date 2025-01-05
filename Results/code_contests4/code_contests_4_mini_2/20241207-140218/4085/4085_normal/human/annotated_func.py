#State of the program right berfore the function call: N is an integer such that 2 <= N <= 10^5, and A is a list of N integers where each integer A_i satisfies 1 <= A_i <= 10^9.
def func_1():
    n = int(input())
    a = sorted(readlist())
    gcd_arr = [0] * (n + 1)
    for i in range(n):
        gcd_arr[i + 1] = gcd(gcd_arr[i], a[i])
        
    #State of the program after the  for loop has been executed: `gcd_arr` is a list where `gcd_arr[i]` contains the gcd of the first `i` elements of `a`, for `1 <= i <= n`; `N` is an integer such that 2 <= N <= 10^5; `n` is an integer greater than or equal to 1.
    gcd_arr_rev = [0] * (n + 1)
    for i in reversed(range(n)):
        gcd_arr_rev[i] = gcd(gcd_arr_rev[i + 1], a[i])
        
    #State of the program after the  for loop has been executed: `gcd_arr` is a list where `gcd_arr[i]` contains the gcd of the first `i` elements of `a` for `1 <= i <= n`; `N` is an integer such that 2 <= N <= 10^5; `n` is an integer greater than or equal to 1; `gcd_arr_rev` is a list where `gcd_arr_rev[i]` contains the gcd of the elements from `a[i]` to `a[n-1]` for `0 <= i < n`.
    res = 0
    for i in range(n):
        res = max(res, gcd(gcd_arr[i], gcd_arr_rev[i + 1]))
        
    #State of the program after the  for loop has been executed: `gcd_arr` is a list where `gcd_arr[0]` contains the gcd of the first element of `a`, `gcd_arr_rev` is a list where `gcd_arr_rev[n]` contains the gcd of the elements from `a[n-1]` to `a[n-1]`, `res` is the maximum gcd value computed from pairs of `gcd_arr[i]` and `gcd_arr_rev[i + 1]` for `0 <= i < n - 1`, `n` is the total number of elements in `a`.
    func_2(res)
#Overall this is what the function does:The function accepts an integer `N` and a list `A` of `N` integers, where `N` satisfies `2 <= N <= 10^5` and each integer in `A` satisfies `1 <= A_i <= 10^9`. It computes the maximum GCD of any two non-overlapping subsets of the list `A` by calculating the GCD of prefix and suffix segments of the sorted list `A`. The result is then passed to another function, `func_2(res)`, but the actual output of `func_1` is not returned and remains undefined.

#State of the program right berfore the function call: N is an integer such that 2 <= N <= 10^5, and A is a list of N integers where each A[i] is between 1 and 10^9 (inclusive).
def func_2():
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 2 <= `N` <= 10^5; `A` is a list of `N` integers between 1 and 10^9; `sep` is written to `file` between each element of `args` except before the first; `file` contains the string representation of all elements in `args` separated by `sep`; `at_start` is False; `args` is a non-empty iterable with at least `N` elements; `x` is the last element in `args` written to `file`.
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`N` is an integer such that 2 <= `N` <= 10^5; `A` is a list of `N` integers between 1 and 10^9; `sep` is written to `file` between each element of `args` except before the first; `file` contains the string representation of all elements in `args` separated by `sep` along with the value from `kwargs` for 'end' or a newline; `at_start` is False; `args` is a non-empty iterable with at least `N` elements; `x` is the last element in `args` written to `file`; if the value of 'flush' was True, then the file has been flushed. Otherwise, there are no changes made to the file.
#Overall this is what the function does:The function accepts a variable number of arguments and keyword arguments, writes the string representation of each argument to a specified file with a specified separator, and appends an end character. If the `flush` keyword argument is true, it flushes the output buffer. It assumes that there are at least two arguments and handles the output formatting accordingly.

