#State of the program right berfore the function call: The function `func_1` does not take any parameters.
def func_1():
    return sys.stdin.readline().strip()
    #The program returns a string that is the next line of input from the standard input, with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_1` reads the next line from the standard input, removes any leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: This function does not have any parameters, so there are no variables or relationships to describe.
def func_2():
    return int(func_1())
    #The program returns the integer value returned by the function `func_1()`
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns the integer value returned by the function `func_1`.

#State of the program right berfore the function call: No specific variables are provided in the function signature for `func_3`. It is assumed that `func_1` returns a string that can be split into integers, which are then converted to a list of integers.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers, which are the integer representations of the substrings obtained by splitting the string returned by `func_1()` on whitespace.
#Overall this is what the function does:The function `func_3` accepts no parameters and returns a list of integers. These integers are derived by splitting a string returned by `func_1()` on whitespace and converting each substring to an integer.

#State of the program right berfore the function call: n is an integer representing the number of players such that 2 <= n <= 1000, m is an integer representing the number of throws such that 1 <= m <= 1000, and x is an integer representing the starting player such that 1 <= x <= n.
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
        
    #State: `n`, `m`, `x` are the same as in the initial state, and `ans` is a set of values derived from repeatedly applying the operations `(q + r) % n` and `(q - r) % n` based on the values of `c` over `m` iterations.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: `n`, `m`, `x` are the same as in the initial state, and `ans` is a set of values derived from repeatedly applying the operations `(q + r) % n` and `(q - r) % n` based on the values of `c` over `m` iterations. If `0` was in `ans`, it is now excluded, and `n` is included in `ans`. Otherwise, `ans` remains unchanged.
    print(len(ans))
    #This is printed: len(ans) (where ans contains n and possibly other unique values derived from the operations, with 0 excluded if it was present)
    print(*sorted(ans))
    #This is printed: the sorted values of the set `ans` (which includes `n` and possibly other values derived from the operations, with `0` excluded if it was present)
#Overall this is what the function does:The function calculates and prints the number of unique players who will receive a throw after `m` throws, starting from player `x`. It prints the count of these unique players and their sorted identifiers, with player `n` replacing player `0` if `0` is among the unique players.

