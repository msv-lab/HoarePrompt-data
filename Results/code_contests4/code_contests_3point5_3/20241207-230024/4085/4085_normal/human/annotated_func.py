#State of the program right berfore the function call: N is an integer such that 2 <= N <= 10^5, and A_i are integers such that 1 <= A_i <= 10^9 for 1 <= i <= N.**
def func_1():
    n = int(input())
    a = sorted(readlist())
    gcd_arr = [0] * (n + 1)
    for i in range(n):
        gcd_arr[i + 1] = gcd(gcd_arr[i], a[i])
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 2 <= N <= 10^5, `gcd_arr` is a list of size N+1 with `gcd_arr[1]` being the GCD of all elements in the list `a`, `i` is N-1
    gcd_arr_rev = [0] * (n + 1)
    for i in reversed(range(n)):
        gcd_arr_rev[i] = gcd(gcd_arr_rev[i + 1], a[i])
        
    #State of the program after the  for loop has been executed: Output State: `N` is an integer such that 3 <= N <= 10^5, `gcd_arr` is a list of size N+1 with `gcd_arr[1]` being the GCD of all elements in the list `a`, `i` is -1, `gcd_arr_rev` is a list of size N+1 with updated values based on the given calculation from the loop.
    res = 0
    for i in range(n):
        res = max(res, gcd(gcd_arr[i], gcd_arr_rev[i + 1]))
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 3 <= N <= 10^5, `gcd_arr` is a list of size N+1 with `gcd_arr[1]` being the GCD of all elements in the list `a`, `i` is N-1, `gcd_arr_rev` is a list of size N+1 with updated values based on the given calculation from the loop, `res` is the maximum value between the calculated GCDs in each iteration of the loop
    func_2(res)
#Overall this is what the function does:The function `func_1` reads an integer `N` and a list of integers `A` of size `N`. It then calculates the Greatest Common Divisor (GCD) of elements in the list `A` in two directions, forwards and backwards. After computing the GCDs, it finds the maximum GCD between the two calculated arrays and passes this result to `func_2` as a parameter. The function does not accept any explicit parameters but relies on the user to input `N` and `A` during execution.

#State of the program right berfore the function call: **Precondition**: **N is an integer such that 2 <= N <= 10^5, A_i are integers such that 1 <= A_i <= 10^9, for 1 <= i <= N.**
def func_2():
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `sep` is assigned the value of the key 'sep' in `kwargs` or `b' '`, `file` is assigned the value of the key 'file' in `kwargs` or `sys.stdout`, `at_start` is False, and `args` is empty
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`sep` is assigned the value of the key 'sep' in `kwargs` or `b' '`, `file` is assigned the value of the key 'file' in `kwargs` or `sys.stdout`, `at_start` is False, `args` is empty, the value of 'end' key in `kwargs` is written to the `file`, and if 'flush' key exists in `kwargs` and its value is True, then 'flush' key is removed from `kwargs`.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It assigns values to `sep` and `file` based on the provided key-value pairs in `kwargs`. It then iterates over the elements in `args`, writing them to the `file` separated by the specified separator `sep`. After the loop, it writes the value of the 'end' key in `kwargs` to the `file`. If the 'flush' key exists in `kwargs` and is set to True, it flushes the `file`. The function does not return any value.

