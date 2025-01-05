#State of the program right berfore the function call: t is an integer between 1 and 100, n is an integer between 1 and 10^5, x is an integer between 2 and 10^9, and a is a list of integers where each integer a_i is between 1 and 10^9. The sum of all n across test cases does not exceed 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer between 1 and 100, `pow_x` is a list of integers where each element `pow_x[i]` is the count of how many times the `i`-th element of `a` is divisible by `x`, `min_pow` is the minimum value from `pow_x`, `min_idx` is the index of the first occurrence of `min_pow` in `pow_x`; and `func_2` has been called multiple times with the argument `sum(a) * (min_pow + 1) + sum(a[:min_idx])` for each iteration of the loop.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases, and for each test case, it takes two integers `n` (the size of a list) and `x`, followed by a list `a` of `n` integers. It calculates how many times each element in `a` can be divided by `x` and determines the minimum count of divisions across the list. It then calls `func_2` with a computed value based on the sum of the list multiplied by one more than this minimum count, plus the sum of the elements in `a` up to the index of the first occurrence of the minimum count. The function does not return any value; instead, it invokes another function (`func_2`) multiple times without handling or returning the result of those calls.

#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100), n is a positive integer (1 ≤ n ≤ 10^5), x is an integer (2 ≤ x ≤ 10^9), and a is a list of integers where each integer a_i is within the range (1 ≤ a_i ≤ 10^9). The total number of elements across all test cases does not exceed 10^5.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `t` is a positive integer (1 ≤ t ≤ 100), `n` is a positive integer (1 ≤ n ≤ 10^5), `x` is the last value from `args`, `a` is a list of integers where each integer `a_i` is within the range (1 ≤ a_i ≤ 10^9), `at_start` is False; all values from `args` have been written to the file using `file.write(str(x))` for each iteration of the loop.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`t` is a positive integer (1 ≤ t ≤ 100), `n` is a positive integer (1 ≤ n ≤ 10^5), `x` is the last value from `args`, `a` is a list of integers where each integer `a_i` is within the range (1 ≤ a_i ≤ 10^9), `at_start` is False; if the flush keyword argument was set to True, then `file.flush()` has been called, ensuring that any buffered output to the file is written out to the file immediately.
#Overall this is what the function does:The function accepts a variable number of arguments and keyword arguments. It prints each argument to the specified output file, separated by a specified separator, and ends with a specified ending character. It also has the option to flush the output buffer. The function does not process the parameters `t`, `n`, `x`, or `a` directly; these are mentioned in the annotations but are not utilized within the function itself.

