#State of the program right berfore the function call: This function does not take any parameters and thus has no preconditions related to input variables.
def func_1():
    return sys.stdin.readline().strip()
    #The program returns a string that is the input provided by the user, with any leading or trailing whitespace removed.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads a line of input from the standard input (stdin), removes any leading or trailing whitespace from the input, and returns the resulting string. The final state of the program after the function concludes is that it has a string containing the user's input with whitespace trimmed.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function `func_1` should return an integer value.
def func_2():
    return int(func_1())
    #The program returns an integer value that is the result of calling `func_1()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It returns an integer value that is the result of calling `func_1()`.

#State of the program right berfore the function call: This function does not have any input parameters.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting the string returned by `func_1()` and converting each split part to an integer.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns a list of integers. This list is obtained by splitting the string returned by `func_1()` and converting each split part to an integer.

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
        
    #State: `n` remains unchanged with the constraint 2 <= n <= 1000, `m` remains unchanged with the constraint 1 <= m <= 1000, `x` remains unchanged with the constraint 1 <= x <= n, `ans` is a set containing all unique values of the form `(q + r) % n` and `(q - r) % n` for each `q` in the set `ans` from the previous iteration if `c` is '1' or '?', or all unique values of the form `(q + r) % n` if `c` is '0', for each of the `m` iterations. `r` and `c` are the integer and string values, respectively, returned by `func_1().split()` during each iteration of the loop.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: *`n` remains unchanged with the constraint 2 <= n <= 1000, `m` remains unchanged with the constraint 1 <= m <= 1000, `x` remains unchanged with the constraint 1 <= x <= n, `ans` is a set containing all unique values of the form `(q + r) % n` and `(q - r) % n` for each `q` in the set `ans` from the previous iteration if `c` is '1' or '?', or all unique values of the form `(q + r) % n` if `c` is '0', for each of the `m` iterations. If 0 is in `ans`, then 0 is removed from `ans` and `n` is included in `ans`. Otherwise, `ans` remains unchanged.
    print(len(ans))
    #This is printed: len(ans) (where `ans` is the set of unique values modulo `n` after `m` iterations, and if 0 is in `ans`, it is replaced by `n`)
    print(*sorted(ans))
    #This is printed: sorted list of unique values from the set `ans` (where `ans` contains values derived from the operations \((q + r) \% n\) and \((q - r) \% n\) if `c` is '1' or '?', or \((q + r) \% n\) if `c` is '0', and does not include `0` but may include `n`)
#Overall this is what the function does:The function `func_4` accepts no parameters but relies on the values of `n`, `m`, and `x` returned by `func_3`. It performs a series of operations over `m` iterations, where in each iteration, it updates a set `ans` based on the values returned by `func_1`. The set `ans` initially contains the value `x` and is updated to include all unique values of the form `(q + r) % n` and `(q - r) % n` for each `q` in `ans` if `c` is '1' or '?', or only values of the form `(q + r) % n` if `c` is '0'. After `m` iterations, if `0` is in `ans`, it is removed and `n` is added to `ans`. The function then prints the length of `ans` and a sorted list of the values in `ans`. The final state of the program is that `n`, `m`, and `x` remain unchanged, and `ans` contains the unique values derived from the operations described, possibly including `n` but not `0`.

