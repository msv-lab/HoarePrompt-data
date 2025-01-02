#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 2 ≤ n ≤ 10^5, c is a list of n integers where 2 ≤ c_i ≤ 10^9, a and b are lists of n integers each, where a[i] and b[i] are such that a[i] and b[i] are valid indices within the range of c[i-1] (inclusive), and the sum of n over all test cases doesn't exceed 10^5.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        c = [int(ci) for ci in input().split()]
        
        a = [int(ai) for ai in input().split()]
        
        b = [int(bi) for bi in input().split()]
        
        for i in range(n):
            a[i], b[i] = min(a[i], b[i]), max(a[i], b[i])
        
        best = 1
        
        curr = b[1] - a[1] + 1
        
        for i in range(1, n):
            best = max(best, curr + c[i])
            if i != n - 1:
                curr += a[i + 1] + (c[i] - b[i + 1] + 1)
                if a[i + 1] == b[i + 1]:
                    curr = 1
        
        func_2(best)
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer, `n` is a non-negative integer, `best` is the maximum value obtained by iterating through the loop, `curr` is 1 if `a[n] == b[n]`, otherwise `curr` is the sum of all increments calculated during the loop, `a[i]` is the minimum of the original `a[i]` and `b[i]` after all iterations, `b[i]` is the maximum of the original `a[i]` and `b[i]` after all iterations, `i` is `n`, `a`, `b`, and `c` are unchanged from their initial values, `func_2(best)` has been called.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t`, another integer `n`, a list `c` of length `n`, and two lists `a` and `b` also of length `n`. For each test case, it first ensures that the elements of `a` and `b` are in ascending order (i.e., `a[i]` is the minimum and `b[i]` is the maximum of the original pair). It then iterates through the list `c` to calculate the maximum possible value `best` by considering the intervals defined by `a` and `b`. Specifically, it calculates the sum of lengths of intervals defined by consecutive pairs `(a[i], b[i])` and adds the corresponding values from `c`. If the interval length is zero, it resets the current sum to 1. After processing all test cases, it calls `func_2` with the maximum value `best` found. The function does not return a value directly but relies on `func_2` to handle the result. Potential edge cases include when `a[i]` equals `b[i]` for any `i`, which results in a single point interval, and when `t` or `n` are at their upper bounds.

#State of the program right berfore the function call: t is an integer representing the number of test cases, n is an integer representing the number of chains, c is a list of integers where c[i] represents the number of vertices in the i-th chain, a is a list of integers where a[i] represents the vertex index in the (i - 1)-th chain that connects to the first vertex of the i-th chain, and b is a list of integers where b[i] represents the vertex index in the (i - 1)-th chain that connects to the last vertex of the i-th chain.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` is an empty iterable, `t` is an integer representing the number of test cases, `n` is an integer representing the number of chains, `c` is a list of integers where `c[i]` represents the number of vertices in the i-th chain, `a` is a list of integers where `a[i]` represents the vertex index in the (i-1)-th chain that connects to the first vertex of the i-th chain, `b` is a list of integers where `b[i]` represents the vertex index in the (i-1)-th chain that connects to the last vertex of the i-th chain, `sep` is a space `' '`, `file` is `sys.stdout`, and `at_start` is `False`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is an empty iterable, `t` is an integer representing the number of test cases, `n` is an integer representing the number of chains, `c` is a list of integers where `c[i]` represents the number of vertices in the i-th chain, `a` is a list of integers where `a[i]` represents the vertex index in the (i-1)-th chain that connects to the first vertex of the i-th chain, `b` is a list of integers where `b[i]` represents the vertex index in the (i-1)-th chain that connects to the last vertex of the i-th chain, `sep` is a space `' '`, `file` is `sys.stdout`, `at_start` is `False`, and `sys.stdout` has been flushed if `kwargs.pop('flush', False)` is `True`. Otherwise, `sys.stdout` remains unchanged.
#Overall this is what the function does:The function takes five parameters: `t`, `n`, `c`, `a`, and `b`. It does not process these parameters directly but instead prints the values of these parameters to the standard output stream (`sys.stdout`). The function writes each parameter value followed by a space and continues without a newline until all parameters are printed. After the loop, it appends a newline character to the output. If the `flush` keyword argument is set to `True`, it flushes the output buffer. If no `sep` or `end` keyword arguments are provided, their default values are a space and a newline, respectively. The function does not return anything. However, it modifies the `sys.stdout` stream by appending the formatted string and flushing the buffer if required.

