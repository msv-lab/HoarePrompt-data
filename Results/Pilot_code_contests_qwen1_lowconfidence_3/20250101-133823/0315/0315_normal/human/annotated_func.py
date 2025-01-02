#State of the program right berfore the function call: t is an integer representing the number of test cases, n is an integer such that 2 <= n <= 3 * 10^5, and a is a list of n integers representing the sizes of the piranhas in the aquarium, where 1 <= a_i <= 10^9. The sum of all n across all test cases does not exceed 3 * 10^5.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        m = max(a)
        
        f = 0
        
        for i in range(n):
            if a[i] == m:
                if i - 1 >= 0 and a[i] > a[i - 1] or i + 1 < n and a[i] > a[i + 1]:
                    func_2(i + 1)
                    f = 1
                    break
        
        if f == 0:
            func_2(-1)
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `n` is an integer input by the user, `a` is a list of integers input by the user, `m` is the maximum value in the list `a`, `f` is 1 if any element in `a` satisfies the condition `(a[i] == m and (i - 1 >= 0 and a[i] > a[i - 1] or i + 1 < n and a[i] > a[i + 1]))` during the loop, otherwise `f` is 0, and `i` is the index of the first occurrence of `m` that satisfies the condition if `f` is 1, otherwise `i` is `n`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of piranhas (`n`) and their sizes stored in a list (`a`). For each test case, it determines whether any piranha with the maximum size (`m`) is adjacent to another piranha that is smaller than it. If such a piranha is found, the function calls `func_2` with the index of the first such piranha. If no such piranha is found, it calls `func_2` with `-1`. The function does not return anything but performs these checks for all test cases.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. Each test case consists of n (2 ≤ n ≤ 3 ⋅ 10^5) positive integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9) representing the sizes of piranhas in the aquarium. The sum of n across all test cases does not exceed 3 ⋅ 10^5 (∑ n ≤ 3 ⋅ 10^5). The function `func_2` is not related to solving the problem and is likely a utility function for printing, which is not used in the provided code snippet.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `sep` is ' ', `file` is `sys.stdout`, `args` contains all input arguments, `at_start` is `False`, each element in `args` is written to `file` with `sep` separating them except the first element.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`t` is a positive integer, `sep` is ' ', `file` is `sys.stdout`, `args` contains all input arguments, `at_start` is `False`, each element in `args` is written to `file` with `sep` separating them except the first element, `sys.stdout` has written `\n`, and if the `kwargs.pop('flush', False)` evaluates to `True`, the buffer of `sys.stdout` is flushed.
#Overall this is what the function does:The function does not accept any parameters and does not return anything. It takes a sequence of arguments (`args`) and writes them to `sys.stdout` separated by a space (`' '`), except for the first element. If the `kwargs` contain an `end` key, it appends its value (defaulting to `\n`) to the output. If the `kwargs` contain a `flush` key set to `True`, it flushes the output buffer of `sys.stdout`. This function can be used to print a list or tuple of values to the standard output with specific formatting options. However, since the function is not called within the provided code snippet, its primary purpose is to demonstrate or test the formatting capabilities for printing.

