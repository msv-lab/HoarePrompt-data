#State of the program right berfore the function call: t is an integer within the range 1 ≤ t ≤ 100, n is a positive integer within the range 1 ≤ n ≤ 10^5, x is an integer within the range 2 ≤ x ≤ 10^9, and a is a list of integers where each integer a_i is within the range 1 ≤ a_i ≤ 10^9. The sum of values n over all test cases does not exceed 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is within the range 1 to 100, `n` is greater than 0, `a` is a list of integers with `n` elements, `pow_x` is a list of integers where each element represents the maximum number of times the corresponding element in `a` can be divided by `x`, `min_pow` is the minimum value from `pow_x`, `min_idx` is the index of `min_pow` in `pow_x`; `func_2` is called with a computed value based on these variables for each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each test case it reads two integers `n` and `x`, then reads a list of `n` integers. It calculates the maximal power of `x` that divides each integer in the list, finds the minimum power, and identifies its index. Based on these values, it calls another function `func_2` with a computed value derived from the sum of the list and the minimum power. The function does not return any value.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 1 ≤ n ≤ 10^5, x is an integer such that 2 ≤ x ≤ 10^9, and a is a list of integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The total length of all arrays across all test cases does not exceed 10^5.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `t` is an integer such that 1 ≤ `t` ≤ 100; `args` is a list of integers; `sep` has been written to the file `n-1` times if `args` has at least 1 element; all elements of `args` have been written to the file as strings; `at_start` is False.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`t` is an integer such that 1 ≤ `t` ≤ 100; `args` is a list of integers; `sep` has been written to the file `n-1` times if `args` has at least 1 element; all elements of `args` have been written to the file as strings; `at_start` is False; a value has been written to the file (either the value of 'end' from kwargs or '\n'); if the flush option from kwargs has been set to True, the file has been flushed to ensure all buffered data is written out.
#Overall this is what the function does:The function accepts a variable number of arguments (args) and keyword arguments (kwargs), where it prints the elements of args to a specified output stream (defaulting to sys.stdout). It separates the elements with a specified separator (defaulting to a space) and terminates the output with a specified end character (defaulting to a newline). If the flush option is set to True, it ensures that all buffered data is written out. The function does not explicitly handle any test case evaluation or constraints related to the inputs, contrary to the annotations, which suggest it processes multiple test cases.

