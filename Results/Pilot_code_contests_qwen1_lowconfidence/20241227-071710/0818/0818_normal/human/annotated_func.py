#State of the program right berfore the function call: t is an integer representing the number of test cases, n is an integer representing the length of the array a, and a is a list of integers representing the array itself. Each element of a is an integer in the range [-10^9, 10^9].
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = [int(i) for i in input().split()]
        
        mx = 0
        
        p = a[0]
        
        for i in range(1, n):
            if a[i] < p:
                mx = max(mx, (p - a[i]).bit_length())
                a[i] = p
            p = a[i]
        
        func_2(mx)
        
    #State of the program after the  for loop has been executed: Output State:
#Overall this is what the function does:The function `func_1` accepts an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list `a` of integers. It then iterates through the list `a` and updates elements in the list such that each element is not less than the previous one (`p`). During this process, it keeps track of the maximum difference (in terms of bit length) between consecutive elements in the list that were adjusted. After processing each test case, it calls `func_2` with this maximum difference. The function does not return anything explicitly, but it modifies the input list `a` in place and calls `func_2` with the computed maximum difference. Potential edge cases include empty lists or lists with a single element, which do not require any adjustments. If the list is already non-decreasing, no adjustments are made.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. Each test case consists of an integer n followed by a list of n integers a, where 1 ≤ t ≤ 10^4 and 1 ≤ n ≤ 10^5. The values of a_i are integers such that -10^9 ≤ a_i ≤ 10^9, and the sum of all n values across all test cases does not exceed 10^5.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `t` is a positive integer greater than 0, `args` is a non-empty list where each element is a tuple `(n, a)` with `n` being an integer and `a` being a list of `n` integers; the file contains the concatenated strings of all tuples `(n, a)` from `args`, with each tuple separated by the string value of `sep`; `at_start` is `False`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`t` is a positive integer greater than 0, `args` is a non-empty list where each element is a tuple `(n, a)` with `n` being an integer and `a` being a list of `n` integers; the file contains the concatenated strings of all tuples `(n, a)` from `args`, with each tuple separated by the string value of `sep`; `at_start` is `False`; the file now contains an additional newline character (`\n`); the 'flush' parameter was popped from `kwargs`, and depending on its value, the file may or may not be flushed.
#Overall this is what the function does:The function processes up to 10,000 test cases, where each test case consists of an integer `n` followed by a list of `n` integers `a`. It concatenates these tuples `(n, a)` into a single string, separating each tuple with the specified separator `sep`. After processing all test cases, it writes an additional newline character to the output file (or stream) and flushes the file if the `flush` parameter is set to `True`. The function does not explicitly return any value but modifies the output file or stream directly. Potential edge cases include handling an empty `args` list or when `sep` or `end` are not provided. However, the code assumes that `args` is non-empty and `sep` and `end` are always provided, which might lead to issues if these assumptions are not met.

