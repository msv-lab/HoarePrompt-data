#State of the program right berfore the function call: h and w are positive integers such that 1 ≤ h, w ≤ 10^3; r is a list of h integers where 0 ≤ r[i] ≤ w for each 0 ≤ i < h; c is a list of w integers where 0 ≤ c[i] ≤ h for each 0 ≤ i < w.
def func_1():
    h, w = map(int, input().split())
    r = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    base = [([0] * w) for _ in range(h)]
    for (i, ri) in enumerate(r):
        for j in range(ri):
            base[i][j] = 1
        
    #State of the program after the  for loop has been executed: `ri` is a list of integers where each `ri[i]` is at most `w` and at least `i + h`, `base[i][j]` where `0 ≤ j < ri[i]` is 1 and `base[i][j]` where `ri[i] ≤ j < w` is 0.
    for (i, ci) in enumerate(c):
        for j in range(ci):
            base[j][i] = 1
        
    #State of the program after the  for loop has been executed: `base[j][i]` is 1 for all valid `j` such that `0 <= j < ci` and `i` is equal to the maximum value of `ci` across all iterations, `i` is a non-negative integer, `ci` is a non-negative integer and is at least the number of times the loop executed.
    for i in range(h):
        if r[i] < w and base[i][r[i]] == 1:
            func_2(0)
            return
        
    #State of the program after the  for loop has been executed: -
    for i in range(w):
        if c[i] < h and base[c[i]][i] == 1:
            func_2(0)
            return
        
    #State of the program after the  for loop has been executed: `w` is greater than 0, for all `i` in the range of `w`, `c[i]` is not less than `h` or `base[c[i]][i]` is not equal to 1, and the function `func_2(0)` is not called, and the return statement is not executed.
    n = 0
    for i in range(1, h):
        for j in range(1, w):
            n += r[i] < j and c[j] < i
        
    #State of the program after the  for loop has been executed: Output State:
    func_2(pow(2, n, 1000000007))
#Overall this is what the function does:The function processes two lists, `r` and `c`, representing the row and column constraints for a grid of size `h` x `w`. It constructs a grid `base` where each element is initially set to 0. For each element in `r`, it marks the first `ri[i]` elements in the corresponding row as 1. Similarly, for each element in `c`, it marks the first `ci[i]` elements in the corresponding column as 1. After marking, it checks if any marked cell violates the constraints and calls `func_2(0)` if such a violation is found. If no violations are found, it counts the number of cells that do not violate the constraints and returns the result of `func_2` applied to \(2^n \mod 1000000007\), where \(n\) is the count of such cells. If no violations are found and `n` is zero, the function returns `None`.

#State of the program right berfore the function call: h and w are integers such that 1 ≤ h, w ≤ 10^3, r is a list of h integers where 0 ≤ r_i ≤ w for all 1 ≤ i ≤ h, and c is a list of w integers where 0 ≤ c_j ≤ h for all 1 ≤ j ≤ w.
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `h` is an integer such that \(1 \leq h \leq 10^3\), `w` is an integer such that \(1 \leq w \leq 10^3\), `r` is a list of `h` integers where \(0 \leq r_i \leq w\) for all \(1 \leq i \leq h\), `c` is a list of `w` integers where \(0 \leq c_j \leq h\) for all \(1 \leq j \leq w\), `sep` is either a value from `kwargs` or a space `' '`, `file`'s content is the concatenation of `str(x)` for all `x` in `args`, `at_start` is `False`, `args` is an empty list.
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *`h` is an integer such that \(1 \leq h \leq 10^3\), `w` is an integer such that \(1 \leq w \leq 10^3\), `r` is a list of `h` integers where \(0 \leq r_i \leq w\) for all \(1 \leq i \leq h\), `c` is a list of `w` integers where \(0 \leq c_j \leq h\) for all \(1 \leq j \leq w\), `sep` is either a value from `kwargs` or a space `' '`, `file`'s content is the concatenation of `str(x)` for all `x` in `args` followed by `\n`, `at_start` is `False`, `args` is an empty list, `kwargs` no longer contains the key `'flush'` with the value `False`, and the write buffer of `file` is flushed if the key `'flush'` with the value `False` was present in `kwargs`. If not, the write buffer remains unchanged.
#Overall this is what the function does:The function `func_2` takes a variable number of arguments (`args`), keyword arguments (`kwargs`), and predefined lists `h`, `w`, `r`, and `c` as input. It prints each argument separated by a separator (`sep`) and ends with an end character (`end`). The function does not return any value. The separator defaults to a space, and the end character defaults to a newline. Additionally, if the `flush` keyword is set to `True`, it flushes the output buffer. The function modifies the content of the file object pointed to by `file` (defaulting to `sys.stdout`), but does not change the values of `h`, `w`, `r`, or `c`. After executing, `args` will be an empty list, `sep` and `end` will reflect the keyword arguments passed, and the output buffer will contain the concatenated string of the arguments separated by `sep` and ending with `end`.

