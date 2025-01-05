#State of the program right berfore the function call: t is an integer (1 ≤ t ≤ 100) indicating the number of test cases; for each test case, n is an integer (1 ≤ n ≤ 10^5) representing the length of the array, and x is an integer (2 ≤ x ≤ 10^9); the array a contains n integers (1 ≤ a_i ≤ 10^9).
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
        
    #State of the program after the  for loop has been executed: `t` is an integer (1 ≤ `t` ≤ 100), `a` is a list of integers of length `n`, `pow_x` is a list of integers where each element represents the count of how many times the corresponding element in `a` can be divided by `x`, `min_pow` is the minimum value from `pow_x`, `min_idx` is the index of the first occurrence of `min_pow` in `pow_x`, and `func_2` is called with the argument `sum(a) * (min_pow + 1) + sum(a[:min_idx])`.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it reads two integers `n` (the length of an array) and `x`, followed by an array `a` of `n` integers. It calculates how many times each element in `a` can be divided by `x` and tracks the minimum count. Finally, it calls another function `func_2` with a calculated value based on the sum of the array and the minimum count. The function does not return any results directly but invokes `func_2`, which is expected to handle the final output.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 1 ≤ n ≤ 10^5 and x is an integer such that 2 ≤ x ≤ 10^9; a is a list of integers where each element a_i satisfies 1 ≤ a_i ≤ 10^9. The total sum of n over all test cases does not exceed 10^5.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `at_start` is False, `args` is a list of arguments, `x` has been written to the file for each element in `args`, and a separator has been written before each element except the first.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`at_start` is False, `args` is a list of arguments, `x` has been written to the file for each element in `args`, a separator has been written before each element except the first, and the value written from `kwargs` is either the value of `end` or a newline character. If `flush` was True, the flush operation has been executed.
#Overall this is what the function does:The function accepts variable arguments and keyword arguments, printing the arguments to a specified file with a customizable separator and end character. It handles printing without leading separators and can flush the output if requested. The function does not directly utilize the parameters `t`, `n`, `x`, and `a` as described in the annotations, which are irrelevant to its actual functionality.

