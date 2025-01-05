#State of the program right berfore the function call: **
def func_1():
    n = int(input())
    a = sorted(readlist())
    gcd_arr = [0] * (n + 1)
    for i in range(n):
        gcd_arr[i + 1] = gcd(gcd_arr[i], a[i])
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `a` is a sorted list, `gcd_arr` is a list where each element is the greatest common divisor of the corresponding elements in `a` and the previous element in `gcd_arr, with the first element being 0
    gcd_arr_rev = [0] * (n + 1)
    for i in reversed(range(n)):
        gcd_arr_rev[i] = gcd(gcd_arr_rev[i + 1], a[i])
        
    #State of the program after the  for loop has been executed: Output State: `n` is greater than or equal to 0, `a` is a sorted list, `gcd_arr` has at least 1 element, `gcd_arr_rev` has a length of n + 1 with updated values calculated by applying the gcd function in reverse order of the elements in `a`, `i` is 0.
    res = 0
    for i in range(n):
        res = max(res, gcd(gcd_arr[i], gcd_arr_rev[i + 1]))
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `a` is a sorted list, `gcd_arr` has at least 1 element, `gcd_arr_rev` has a length of n + 1 with updated values, `i` is n-1, `res` is the maximum value of gcd_arr and gcd_arr_rev
    func_2(res)
#Overall this is what the function does:The function `func_1` reads an integer `n` from the user input, sorts a list `a` read from an unknown function `readlist()`, calculates two arrays `gcd_arr` and `gcd_arr_rev` representing the greatest common divisors of elements in `a` in forward and reverse order, and then finds the maximum value of the greatest common divisors between corresponding elements in `gcd_arr` and `gcd_arr_rev`. The function calls `func_2` with the result of this calculation.

#State of the program right berfore the function call: **
def func_2():
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `sep` is the value of 'sep' key in `kwargs` or b' ' if not found, `file` is the value of 'file' key in `kwargs` or sys.stdout if not found, `at_start` is False, `args` is an empty list
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`sep` is the value of 'sep' key in `kwargs` or b' ' if not found, `file` is the value of 'file' key in `kwargs` or sys.stdout if not found, `at_start` is False, `args` is an empty list. If kwargs.pop('flush', False) is True, then the function will perform a flush operation. Otherwise, no action is taken.
#Overall this is what the function does:The function `func_2` does not accept any parameters and writes the elements in `args` to the `file` separated by `sep`. If the 'end' key is present in `kwargs`, it writes the corresponding value at the end. If the 'flush' key is True in `kwargs`, it flushes the file.

