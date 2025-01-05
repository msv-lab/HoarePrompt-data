#State of the program right berfore the function call: **Precondition**: **t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the length of the array, x is a positive integer such that 2 <= x <= 10^9, and a_i (1 ≤ a_i ≤ 10^9) are positive integers representing the initial values in the array.**
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
        
    #State of the program after the  for loop has been executed: `t` is decremented by the total number of test cases, all other variables retain their previous values. `func_2` is called with the parameter `sum(a) * (min_pow + 1) + sum(a[:min_idx])` for each test case.
#Overall this is what the function does:The function `func_1` reads input data for multiple test cases where each case consists of an array `a`, the length of the array `n`, and an integer `x`. It then calculates the minimum power of `x` that each element in the array can be divided by, finds the minimum power value, and calls another function `func_2` with a specific parameter for each test case. The function does not have any explicit return value, and its purpose seems to be processing and forwarding test case data to `func_2` based on given constraints.

#State of the program right berfore the function call: **
def func_2():
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop('sep', ' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        
        file.write(str(x))
        
        at_start = False
        
    #State of the program after the  for loop has been executed: `sep` and `file` remain unchanged, `at_start` is False
    file.write(kwargs.pop('end', '\n'))
    if kwargs.pop('flush', False) :
        file.flush()
    #State of the program after the if block has been executed: *The program terminates with a KeyError. If the 'flush' key is present in kwargs, it is removed from kwargs. Otherwise, no changes occur to kwargs.
#Overall this is what the function does:The function func_2 does not accept any parameters and writes the values in args to a stream, with a specified separator and end character. If the 'flush' key is present in the keyword arguments, it will attempt to flush the stream. However, the code may raise a KeyError due to the use of kwargs.pop without a default value.

