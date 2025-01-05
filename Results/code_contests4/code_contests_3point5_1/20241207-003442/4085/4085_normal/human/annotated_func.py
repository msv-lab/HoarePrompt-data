#State of the program right berfore the function call: N is an integer such that 2 <= N <= 10^5, and A_i is an integer such that 1 <= A_i <= 10^9 for 1 <= i <= N.**
def func_1():
    n = int(input())
    a = sorted(readlist())
    gcd_arr = [0] * (n + 1)
    for i in range(n):
        gcd_arr[i + 1] = gcd(gcd_arr[i], a[i])
        
    #State of the program after the  for loop has been executed: N is an integer such that 2 <= N <= 10^5, A_i is an integer such that 1 <= A_i <= 10^9 for 1 <= i <= N, a is a sorted list of integers from readlist(), gcd_arr is a list where gcd_arr[i + 1] is the greatest common divisor of gcd_arr[i] and a[i] for 0 <= i < N
    gcd_arr_rev = [0] * (n + 1)
    for i in reversed(range(n)):
        gcd_arr_rev[i] = gcd(gcd_arr_rev[i + 1], a[i])
        
    #State of the program after the  for loop has been executed: N is an integer such that 2 <= N <= 10^5, A_i is an integer such that 1 <= A_i <= 10^9 for 1 <= i <= N, a is a sorted list of integers from readlist(), gcd_arr is a list where gcd_arr[i + 1] is the greatest common divisor of gcd_arr[i] and a[i] for 0 <= i < N, gcd_arr_rev is a list of updated greatest common divisors in reverse order
    res = 0
    for i in range(n):
        res = max(res, gcd(gcd_arr[i], gcd_arr_rev[i + 1]))
        
    #State of the program after the  for loop has been executed: N is an integer such that 2 <= N <= 10^5, A_i is an integer such that 1 <= A_i <= 10^9 for 1 <= i <= N, a is a sorted list of integers from readlist(), gcd_arr is a list where gcd_arr[i + 1] is the greatest common divisor of gcd_arr[i] and a[i] for 0 <= i < N, gcd_arr_rev is a list of updated greatest common divisors in reverse order, res is the maximum value between all combinations of gcd_arr and gcd_arr_rev
    func_2(res)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `a`, sorts `a`, calculates the greatest common divisors of elements in `a` in both forward and reverse directions, then finds the maximum value among combinations of these greatest common divisors. It then calls `func_2` with the maximum value as an argument. The function does not accept any parameters and operates within predefined constraints for `n` and `a`.

#State of the program right berfore the function call: **
def func_2():
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `sep` is the popped value, `file` is the popped value with all elements from `args` written to it separated by `sep`, `at_start` is False, `args` is an empty list
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`sep`, `file`, `args` are popped values and `at_start` is False. If 'flush' is True in kwargs, then the file is flushed after writing all elements from `args` separated by `sep` and 'end' value to it. Otherwise, no operation is performed.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It initializes `sep` and `file` values by popping from `kwargs`. It then iterates through the elements in `args`, writing them to the `file` separated by `sep`. The function sets `at_start` to False after the first element is written. Finally, it appends the value of 'end' to the file and flushes the file if 'flush' is True in `kwargs`. This function performs operations on the file based on the provided `kwargs` but does not have a return value.

