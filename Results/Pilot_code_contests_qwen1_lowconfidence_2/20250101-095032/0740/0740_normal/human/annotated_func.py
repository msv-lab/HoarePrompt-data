#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^5. x is a list of k positive integers such that 1 ≤ x_i ≤ n for each i from 1 to k.
def func_1():
    n, k = readlist()
    x = readlist()
    counter = [(-1, -1)] * (n + 1)
    for (i, xi) in enumerate(x):
        if counter[xi][0] == -1:
            counter[xi] = i, -1
        else:
            counter[xi] = counter[xi][0], i
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \(1 \leq n \leq 10^5\), `k` is a positive integer such that \(1 \leq k \leq 10^5\), `x` is a list of `k` positive integers such that \(1 \leq x_i \leq n\) for each \(i\) from 1 to \(k\), `counter` is a list of tuples where for each `xi` in `x`, if `xi` appears for the first time, `counter[xi]` is set to `(i, -1); otherwise, `counter[xi]` remains unchanged.
    res = 0
    for i in range(1, n + 1):
        if counter[i][0] == -1:
            res += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \(1 \leq n \leq 10^5\), `k` is a positive integer such that \(1 \leq k \leq 10^5\), `x` is a list of `k` positive integers where each integer is between 1 and `n`, `counter` is initialized appropriately based on the elements in `x`, `res` is the count of unique elements in `x`.
    for i in range(1, n):
        if counter[i][0] != -1:
            if counter[i][1] != -1:
                if counter[i + 1][0] == -1 or counter[i + 1][0] > counter[i][1]:
                    res += 1
            elif counter[i + 1][0] == -1 or counter[i + 1][0] > counter[i][0]:
                res += 1
        else:
            res += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \(1 \leq n \leq 10^5\), `k` is a positive integer such that \(1 \leq k \leq 10^5\), `x` is a list of `k` positive integers where each integer is between 1 and `n`, `counter` is initialized appropriately based on the elements in `x`, `res` is the count of unique elements in `x`, `i` is `n`, `n` is greater than 0, and `res` is incremented by 1 for every iteration where the conditions in the loop are met.
    for i in range(1, n):
        if counter[i + 1][0] != -1:
            if counter[i + 1][1] != -1:
                if counter[i][0] == -1 or counter[i][0] > counter[i + 1][1]:
                    res += 1
            elif counter[i][0] == -1 or counter[i][0] > counter[i + 1][0]:
                res += 1
        else:
            res += 1
        
    #State of the program after the  for loop has been executed: `counter` is a list of lists, where each inner list has at least two elements, and `i` is `n`. `res` is incremented by 1 for every iteration where the specified conditions are met, leading to a final value of `res` that reflects the number of times the conditions were satisfied.
    func_2(res)
#Overall this is what the function does:The function `func_1` accepts parameters `n`, `k`, and `x`, where `n` and `k` are positive integers such that \(1 \leq n, k \leq 10^5\), and `x` is a list of `k` positive integers such that \(1 \leq x_i \leq n\) for each \(i\) from 1 to `k`. After executing the function, the program state will be such that `n` and `k` remain unchanged, `x` remains unchanged, and `counter` is a list of tuples where each tuple represents the first and last occurrence index of each element in `x`. The function then calculates and returns the count (`res`) of unique elements in `x` based on specific conditions involving the indices stored in `counter`. The final value of `res` reflects the number of times certain conditions are satisfied throughout the iterations of the loops.

#State of the program right berfore the function call: args is a tuple containing two integers n and k, where 1 ≤ n,k ≤ 10^5, and kwargs is a dictionary with the following possible keys: 'sep' (default value is b' '), 'file' (default value is sys.stdout), 'end' (default value is b'\n'), and 'flush' (default value is False).
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` is a tuple containing two integers `n` and `k`, where \(1 \leq n, k \leq 10^5\), `kwargs` is a dictionary with 'file' set to `sys.stdout` and 'sep' set to `b' '`, `at_start` is `False`, and the strings `str(n)` and `str(k)` have been written to `sys.stdout` separated by a space `b' '`.
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is a tuple containing two integers `n` and `k`, `kwargs` is a dictionary with 'file' set to `sys.stdout` and 'sep' set to `b' '`, `at_start` is `False`, the strings `str(n)` and `str(k)` have been written to `sys.stdout` separated by a space `b' '`, and `b'\n'` has been written to `sys.stdout`. After executing the if statement, `kwargs` no longer contains the key 'flush'.
#Overall this is what the function does:This function accepts a tuple `args` containing two integers `n` and `k`, where \(1 \leq n, k \leq 10^5\), and a dictionary `kwargs` with optional keys for `sep`, `file`, `end`, and `flush`. It prints the values of `n` and `k` to the specified output stream (`file`), separated by a space (`sep`), followed by a newline (`end`). If `flush` is set to `True` in `kwargs`, it flushes the output stream. The function ensures that only valid `kwargs` keys are considered, and any remaining keys in `kwargs` are ignored after processing.

