#State of the program right berfore the function call: No variables in the function signature. The function `func_1` does not take any parameters and returns a string, which is a stripped line read from standard input.
def func_1():
    return sys.stdin.readline().strip()
    #The program returns a string that is a stripped line read from standard input.
#Overall this is what the function does:The function `func_1` reads a line from standard input, removes any leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: This function does not have any parameters in its signature, so there are no variables or relationships to describe.
def func_2():
    return int(func_1())
    #The program returns the integer value returned by the function `func_1()`
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns the integer value returned by the function `func_1()`.

#State of the program right berfore the function call: This function does not have any parameters, and it implicitly relies on the return value of `func_1()`, which is expected to return a string that can be split into a list of integers.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers, which are the result of splitting the string returned by `func_1()` and converting each split substring into an integer.
#Overall this is what the function does:The function `func_3` takes no parameters. It processes the string returned by `func_1()` by splitting it into substrings and converting each substring into an integer. The function then returns a list of these integers.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 1000, m is an integer such that 1 <= m <= 1000, x is an integer such that 1 <= x <= n. r is an integer such that 1 <= r <= n - 1, and c is a character that can be '0', '1', or '?'.
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
        
    #State: `ans` is a set of integers that have been transformed through a series of additions and subtractions modulo `n` based on the values of `r` and `c` obtained from `func_1()` in each of the `m` iterations.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: `ans` is a set of integers that have been transformed through a series of additions and subtractions modulo `n` based on the values of `r` and `c` obtained from `func_1()` in each of the `m` iterations. If `0` was an element in `ans` before the if statement, it is no longer an element in `ans` and `n` is an element in `ans`. If `0` was not an element in `ans`, no changes are made to `ans`.
    print(len(ans))
    #This is printed: len(ans) (where len(ans) is the number of elements in the set `ans` after the described transformations)
    print(*ans)
    #This is printed: n [other elements of ans excluding 0] (where n is definitely in ans and 0 is not in ans if it was originally present)
#Overall this is what the function does:The function performs a series of transformations on an initial set containing a single integer `x` by adding or subtracting a value `r` modulo `n` based on the character `c`. After `m` iterations, it adjusts the set by replacing `0` with `n` if `0` is present. The function then outputs the number of elements in the final set and the elements themselves, ensuring `0` is not present and `n` is included if necessary.

