#State of the program right berfore the function call: t is a positive integer. n is a positive integer less than or equal to 10^5. x is an integer such that 2 <= x <= 10^9. a_i are integers such that 1 <= a_i <= 10^9.**
def func_1():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        
        a = [int(ai) for ai in input().split()]
        
        pow_x = [0] * n
        
        for i, ai in enumerate(a):
            cnt = 0
            while ai % x == 0:
                cnt += 1
                ai //= x
            pow_x[i] = cnt
        
        min_pow = min(pow_x)
        
        min_idx = pow_x.index(min_pow)
        
        func_2(sum(a) * (min_pow + 1) + sum(a[:min_idx]))
        
    #State of the program after the  for loop has been executed: `t` is the number of zeros in the list `pow_x`, `n`, `x` are assigned new values from the last iteration of the loop, `a` is the list containing integers where each element has been divided by `x` till they are no longer divisible, `pow_x` is a list of length `n` filled with the total number of times each element in `a` was divisible by `x` before becoming indivisible, `min_pow` is the minimum value in the list `pow_x`, `min_idx` is the index of the minimum value in the list `pow_x`
#Overall this is what the function does:The function func_1 reads input values, performs calculations on the input data, and calls func_2 with specific arguments. It iterates over a range of t, where t is the number of test cases. For each test case, it calculates the number of times each element in a list can be divided by x, finds the minimum division count, and then calculates a specific value based on this minimum count and indices. However, the actual purpose or expected behavior of the function is not clearly defined.

#State of the program right berfore the function call: t is a positive integer, n is a positive integer, x is an integer such that 2 <= x <= 10^9, a_i are integers such that 1 <= a_i <= 10^9, and the sum of n over all test cases does not exceed 10^5.**
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `at_start` is False, `args` is a list with at least one element
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`at_start` is False, `args` is a list with at least one element, the file has been flushed if kwargs.pop('flush', False) is True.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It iterates over the elements in `args` and prints them to the specified file stream, separating them by the value of `sep`. If `flush` is True in the keyword arguments, it flushes the file. The function does not return any value.

