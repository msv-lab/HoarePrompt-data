#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the number of piranhas, and a is a list of n positive integers where each integer represents the size of a piranha.
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
        
    #State of the program after the  for loop has been executed: `t` is the number of test cases entered by the user, `a` is a list of integers, `f` is 0, `i` is `n`, and `n` is the number of elements in each list `a`. If no element in any of the lists `a` satisfies the condition of being a local maximum equal to `m`, then `f` remains 0 and `func_2(-1)` is called at the end of the loop for each test case. Otherwise, for each list `a`, if there exists an element that is a local maximum (`a[i] == m` and either `i-1 < 0` or `i+1 >= n` or both conditions hold), then `f` is set to 1, `func_2(i + 1)` is called, and the loop breaks.
#Overall this is what the function does:The function accepts a parameter `t`, a positive integer representing the number of test cases. For each test case, it accepts `n`, a positive integer representing the number of piranhas, and `a`, a list of `n` positive integers representing the sizes of the piranhas. The function then iterates through each list `a` and checks if there exists a local maximum element (an element that is larger than its immediate neighbors). If such an element is found, it calls `func_2` with the position of this element plus one and sets a flag `f` to 1. If no such element is found in any of the lists, it calls `func_2` with -1 for each test case. The final state of the program after the function concludes is that `t` remains unchanged, `a` is unchanged, `f` is 0 if no local maximum was found or 1 if at least one local maximum was found, `i` is `n` (the length of the current list `a`), and `n` is the number of elements in each list `a`.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n is an integer representing the number of piranhas in the aquarium, followed by a list of n integers a_1, a_2, ..., a_n where each a_i is the size of the i-th piranha.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `t` is an integer, `n` is an integer, `args` is an empty collection, `sep` is set to `kwargs.pop('sep', ' ')`, `file` is set to `kwargs.pop('file', sys.stdout); `at_start` is `False`. The file contains the concatenation of string representations of all elements in `args` separated by `sep`.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`t` is an integer, `n` is an integer, `args` is an empty collection, `sep` is set to `kwargs.pop('sep', ' ')`, `file` is an instance of `io.TextIOWrapper` with its content being the original content plus `\n`, `at_start` is `False`. If `flush` is `True`, the function flushes the contents of `file`. Otherwise, the state of the variables remains unchanged.
#Overall this is what the function does:The function does not accept any parameters `t` or `n`, nor does it process a list of piranha sizes. Instead, it accepts a variable number of positional arguments (`args`) and keyword arguments (`kwargs`). It prints these arguments to a specified output stream (`file`), separated by a specified separator (`sep`), and appends a specified end character (`end`). If the `flush` argument is set to `True`, it flushes the output stream. After executing, the function leaves `t`, `n`, and `a_i` (if they were present in the input) unchanged, and the output stream contains the concatenated string representations of the input arguments, possibly including separators and end characters. There is no processing of test cases or piranha sizes as implied in the annotations.

