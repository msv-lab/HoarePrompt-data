#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_1():
    return sys.stdin.readline().strip()
    #The program returns a string that is the first line of input read from the standard input, with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_1` reads the first line of input from the standard input, removes any leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: None of the variables in the function signature are relevant to the problem description.
def func_2():
    return int(func_1())
    #The program returns an integer value that is the result of calling `func_1()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer value obtained from calling `func_1`. After the function concludes, the program state is unchanged except for the returned integer value.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting the string returned by `func_1()` and converting each part to an integer.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It returns a list of integers obtained by splitting the string returned by `func_1()` and converting each part to an integer.

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
        
    #State: `n`, `m`, and `x` are the values returned by `func_3()`, `ans` is a set containing all unique values of `(q + r) % n` and `(q - r) % n` for each `q` in the original `ans`, depending on the value of `c`, for all iterations of the loop. `c`, `r`, and `n` remain unchanged, and `_` is the final value of the range, which is `m - 1`.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: *`n`, `m`, and `x` are the values returned by `func_3()`, `ans` is a set containing all unique values of `(q + r) % n` and `(q - r) % n` for each `q` in the original `ans`, depending on the value of `c`, for all iterations of the loop. If `0` is in `ans`, the value `0` is removed from `ans` and `n` is added to `ans`. `c`, `r`, and `n` remain unchanged, and `_` is the final value of the range, which is `m - 1`.
    print(len(ans))
    #This is printed: len(ans) (where `ans` is the set containing all unique values of `(q + r) % n` and `(q - r) % n` for each `q` in the original `ans`, with `0` removed and `n` added if `0` was present, after `m` iterations of the loop)
    print(*ans)
    #This is printed: 1 2 3 4 5 (where 1, 2, 3, 4, 5 are the unique values in the final `ans` set after the loop and condition check)
#Overall this is what the function does:The function `func_4` does not accept any parameters and does not return any values. It initializes a set `ans` with a single element `x`, where `x` is an integer between 1 and `n`. It then iterates `m` times, where `m` is an integer between 1 and 1000. In each iteration, it processes a pair `(r, c)` where `r` is an integer and `c` is a string. Based on the value of `c`, it updates `ans` to include all unique values of `(q + r) % n` and `(q - r) % n` for each `q` in `ans`. After the loop, if `0` is in `ans`, it is removed and `n` is added to `ans`. Finally, the function prints the size of `ans` and all elements in `ans`.

