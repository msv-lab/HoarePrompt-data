#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_1():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the standard input (stdin) with any trailing whitespace removed.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns the first line of input from the standard input (stdin) with any trailing whitespace removed.

#State of the program right berfore the function call: This function does not take any parameters and is assumed to be part of a larger solution where `func_1` returns an integer.
def func_2():
    return int(func_1())
    #The program returns an integer value that is the result of calling `func_1()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer value that is the result of calling `func_1()`. After the function concludes, the program state is such that an integer value, derived from the return value of `func_1()`, is available as the return value of `func_2`.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting the string returned by `func_1()` and converting each element to an integer.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It returns a list of integers obtained by splitting the string returned by `func_1()` and converting each element to an integer.

#State of the program right berfore the function call: n, m, and x are integers such that 2 <= n <= 1000, 1 <= m <= 1000, and 1 <= x <= n.
def func_4():
    n, m, x = func_3()
    ans = {x}
    for _ in range(m):
        r, c = func_1().split()
        
        r = int(r)
        
        temp = set()
        
        for q in ans:
            if c == '0' or c == '?':
                temp.add((q + r) % n)
            if c == '1' or c == '?':
                temp.add((q - r) % n)
        
        ans = temp
        
    #State: After the loop executes all `m` iterations, `n`, `m`, and `x` remain unchanged. `ans` contains all possible results of the operations `(q + r) % n` and `(q - r) % n` for each element `q` in the initial `ans`, depending on the value of `c` during each iteration. If `c` is '0', only the results of `(q + r) % n` are added to `ans`. If `c` is '1', only the results of `(q - r) % n` are added to `ans`. If `c` is '?', both results are added to `ans`. The loop counter `_` is equal to `m`.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: *After the loop executes all `m` iterations, `n`, `m`, and `x` remain unchanged. `ans` contains all possible results of the operations `(q + r) % n` and `(q - r) % n` for each element `q` in the initial `ans`, depending on the value of `c` during each iteration. If `c` is '0', only the results of `(q + r) % n` are added to `ans`. If `c` is '1', only the results of `(q - r) % n` are added to `ans`. If `c` is '?', both results are added to `ans`. The loop counter `_` is equal to `m`. If `0` was an element in `ans`, it is no longer present, and `n` is now an element in `ans`. If `0` was not an element in `ans`, `ans` remains as described above.
    print(len(ans))
    #This is printed: len(ans) (where len(ans) is the number of elements in the list `ans` after `m` iterations, considering the operations and the adjustments for `0` and `n`)
    print(*ans)
    #This is printed: - The exact values in `ans` depend on the initial values of `ans`, `n`, and `r`, as well as the values of `c` during each iteration of the loop.
    #   - However, we can describe the output based on the given conditions.
    #
    #Output:
#Overall this is what the function does:The function `func_4` accepts no parameters and returns no values. It operates on three integers `n`, `m`, and `x` that are initially provided by the function `func_3`. The function computes a set `ans` of integers, starting with the set containing only `x`. Over `m` iterations, it updates `ans` by adding the results of `(q + r) % n` and/or `(q - r) % n` for each `q` in `ans`, where `r` and `c` are obtained from the output of `func_1()`. The operations added to `ans` depend on the value of `c`: if `c` is '0', only `(q + r) % n` is added; if `c` is '1', only `(q - r) % n` is added; if `c` is '?', both are added. After all iterations, if `0` is in `ans`, it is removed and `n` is added. The function then prints the number of elements in `ans` and the elements themselves. The final state of the program is that `n`, `m`, and `x` remain unchanged, and `ans` contains the computed set of integers as described.

