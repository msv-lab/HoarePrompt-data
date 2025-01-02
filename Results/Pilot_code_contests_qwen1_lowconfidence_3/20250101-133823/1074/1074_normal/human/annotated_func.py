#State of the program right berfore the function call: t is an integer representing the number of test cases; n is an integer such that 2 ≤ n ≤ 10^5, indicating the number of chains; c is a list of n integers where 2 ≤ c_i ≤ 10^9, representing the number of vertices in each chain; a and b are lists of n integers where a_i and b_i are such that 1 ≤ a_i, b_i ≤ c_{i-1}, indicating the vertices connected to the first and last vertices of each chain respectively; and t, n, c, a, b are structured as described in the problem statement.
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
        
    #State of the program after the  for loop has been executed: `i` is `n`, `t` is the input integer, `n` is the input integer, `best` is the maximum value of `best` and `curr + c[i]` for all iterations, `a[i]` is the minimum of the original `a[i]` and `b[i]` for all `i` in the range `[0, n)`, `b[i]` is the maximum of the original `a[i]` and `b[i]` for all `i` in the range `[0, n)`, `c` is a list of integers obtained from the input, and `curr` is 1.
#Overall this is what the function does:The function `func_1` accepts an integer `t` representing the number of test cases. For each test case, it reads additional parameters including an integer `n`, a list `c` of integers, and two lists `a` and `b` of integers. It then processes these inputs by updating `a` and `b` to ensure `a[i]` is the minimum and `b[i]` is the maximum of the original `a[i]` and `b[i]`. The function calculates a `best` value which is the maximum sum of consecutive chain lengths starting from the second vertex to the end of each chain, considering the connections defined by `a` and `b`. After processing all test cases, it calls another function `func_2` with the final `best` value. The function ensures that the final state includes the updated values of `a` and `b` for each chain, the `best` value calculated, and the `curr` value set to 1. Potential edge cases include scenarios where `a[i]` equals `b[i]` for any chain, in which case `curr` is reset to 1. The function does not return any value but updates internal states and calls another function with the result.

#State of the program right berfore the function call: t is an integer representing the number of test cases, n is an integer such that 2 ≤ n ≤ 10^5, c_i is an integer such that 2 ≤ c_i ≤ 10^9, a_i is an integer such that a_1 = -1 and 1 ≤ a_i ≤ c_{i-1}, and b_i is an integer such that b_1 = -1 and 1 ≤ b_i ≤ c_{i-1}.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `args` is a list containing at least two elements, `at_start` is `False`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`args` is a list containing at least two elements, `at_start` is `False`, a newline character (`'\n'`) is written to the file. If `kwargs` does not contain the key 'flush' or the value of `flush` is `False`, `file.flush()` has been called. If `kwargs` contains the key 'flush' with any value other than `False`, no additional operations are performed.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It takes a list of arguments (`args`), a separator (`sep`), a file object (`file`), and optional keyword arguments (`kwargs`). The function writes each element of `args` to the specified file, separated by `sep`, and ends with the value of `kwargs['end']`. If `kwargs['flush']` is `True`, it flushes the file buffer. The final state of the program is that the elements of `args` have been written to the file with the specified separator and end character, and the file buffer (if open) has been flushed if requested. Potential edge cases include when `args` is empty or when `kwargs` do not contain certain keys. If `args` is empty, no output will be generated. If `kwargs` does not contain `sep`, `end`, or `flush`, their default values (' ', '\n', and `False`, respectively) will be used.

