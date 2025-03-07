#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_1():
    return sys.stdin.readline().strip()
    #The program returns a string that is read from the standard input, with any leading or trailing whitespace removed.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads a line from the standard input, removes any leading or trailing whitespace from the string, and returns the modified string.

#State of the program right berfore the function call: None, as the function does not take any parameters.
def func_2():
    return int(func_1())
    #The program returns an integer value resulting from the execution of `func_1()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer value that is the result of calling `func_1()`. After the function concludes, the program state is unchanged except for the return value.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting the string returned by `func_1()` and converting each part to an integer.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns a list of integers. This list is obtained by splitting the string returned by `func_1()` and converting each part of the split string to an integer.

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
        
    #State: `n`, `m`, and `x` are the values returned by `func_3()`, `ans` is a set containing all unique values of `(q + r) % n` and `(q - r) % n` for each `q` in the original `ans` for each iteration of the loop, where `r` and `c` are the values returned by `func_1()` in each iteration. `m` is 0, and `temp` is an empty set.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: *`n`, `m`, and `x` are the values returned by `func_3()`, `ans` is a set containing all unique values of `(q + r) % n` and `(q - r) % n` for each `q` in the original `ans` for each iteration of the loop. `m` is 0, and `temp` is an empty set. If `0` is in `ans`, `0` is removed from `ans` and `n` is added to `ans`. Otherwise, `ans` remains unchanged.
    print(len(ans))
    #This is printed: len(ans) (where `ans` is the set after the operations described, and its length will remain unchanged if `0` is not in `ans`, or it will remain the same if `0` is in `ans` and is replaced by `n`)
    print(*sorted(ans))
    #This is printed: - The `print(*sorted(ans))` statement will print the sorted elements of the set `ans`.
    #
    #Since the exact values of `q` and `r` are not provided, and the function `func_3()` is not defined, we can't determine the exact numerical values in `ans`. However, we can describe the output based on the operations and conditions given:
    #
    #- If `0` was in `ans`, it will be removed and `n` will be added.
    #- The final set `ans` will be sorted and printed.
    #
    #Output:
#Overall this is what the function does:The function `func_4` does not accept any parameters and does not return any values. It initializes `n`, `m`, and `x` by calling `func_3()`. It then performs a series of operations based on the values returned by `func_1()` in a loop that runs `m` times. The function maintains a set `ans` which initially contains the value `x`. For each iteration, it updates `ans` to include all unique values of `(q + r) % n` and `(q - r) % n` for each `q` in `ans`, where `r` and `c` are the values returned by `func_1()`. After the loop, if `0` is in `ans`, it is removed and `n` is added to `ans`. Finally, the function prints the length of `ans` and the sorted elements of `ans`.

