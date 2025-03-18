#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_1():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the user, with any leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns the first line of user input, stripped of leading and trailing whitespace.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000, m is an integer such that 1 ≤ m ≤ 1000, x is an integer such that 1 ≤ x ≤ n, and throws is a list of tuples where each tuple contains an integer r_i (1 ≤ r_i ≤ n - 1) and a string c_i ('0', '1', or '?') representing the distance and direction of the throw, respectively.
def func_2():
    return int(func_1())
    #The program returns an integer value, which is the result of converting the output of `func_1()` to an integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer value, which is the result of converting the output of `func_1()` to an integer. The state of the program before the function call, including the variables `n`, `m`, `x`, and `throws`, is not affected by the execution of `func_2`. The purpose of the function is to provide an integer output derived from `func_1()`.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting the string returned by `func_1()` and converting each part to an integer.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns a list of integers. This list is obtained by splitting the string returned by `func_1()` and converting each part to an integer.

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
        
    #State: `ans` is a set containing all integers that can be reached by adding or subtracting multiples of `r` (from the last call of `func_1`) to the initial value `x`, modulo `n`, after `m` iterations. The size of `ans` can vary depending on the values of `r` and `c` from each call of `func_1`.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: *`ans` is a set containing all integers that can be reached by adding or subtracting multiples of `r` to the initial value `x`, modulo `n`, after `m` iterations. If `0` is in `ans`, then `ans` now includes `n` and excludes `0`. Otherwise, `ans` remains unchanged.
    print(len(ans))
    #This is printed: - The `print(len(ans))` statement will print the number of unique elements in the set `ans` after the described modifications.
    #
    #Given the initial state and the operations, the output will be the length of the set `ans` after the modifications. Since the exact values of `x`, `r`, `n`, and `m` are not provided, we can't compute the exact numerical length of `ans`. However, we can describe the output based on the given conditions.
    #
    #Output:
    print(*sorted(ans))
    #This is printed: sorted elements of `ans` (where `ans` is a set of integers that can be reached by adding or subtracting multiples of `r` to `x`, modulo `n`, after `m` iterations, and if `0` is in `ans`, it is replaced by `n`)
#Overall this is what the function does:The function `func_4` takes no parameters and does not return any value. It operates on three integers `n`, `m`, and `x` that are obtained from a call to `func_3`, where `2 <= n <= 1000`, `1 <= m <= 1000`, and `1 <= x <= n`. The function computes a set `ans` of integers that can be reached by adding or subtracting multiples of `r` (obtained from `func_1`) to the initial value `x`, modulo `n`, over `m` iterations. If `0` is in the set `ans` after these iterations, it is removed and `n` is added to the set. The function then prints the number of unique elements in `ans` and the sorted elements of `ans`.

