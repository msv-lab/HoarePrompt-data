#State of the program right berfore the function call: No variables are present in the function signature of `func_1`.
def func_1():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the standard input, stripped of any leading and trailing whitespace.
#Overall this is what the function does:The function `func_1` reads the first line of input from the standard input and returns it after removing any leading and trailing whitespace.

#State of the program right berfore the function call: This function does not have any parameters, so there are no variables or relationships to describe.
def func_2():
    return int(func_1())
    #The program returns the integer value of whatever `func_1()` returns.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns the integer value returned by `func_1`.

#State of the program right berfore the function call: The function `func_3` does not take any parameters and returns a list of integers. The integers in the list are obtained by splitting the input string returned by `func_1` into individual components and converting each component to an integer.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting the input string returned by `func_1` into individual components and converting each component to an integer.
#Overall this is what the function does:The function `func_3` does not take any parameters and returns a list of integers. These integers are obtained by splitting an input string returned by `func_1` into individual components and converting each component to an integer.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 1000, m is an integer such that 1 <= m <= 1000, and x is an integer such that 1 <= x <= n. r is an integer such that 1 <= r <= n - 1, and c is a character that can be '0', '1', or '?'.
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
        
    #State: `ans` is a set of all unique values computed from `(q + r) % n` and `(q - r) % n` for each `q` in the previous `ans` set, based on the `c` values from each iteration; `n`, `m`, `x`, and `r` remain unchanged; `c` is the value from the last iteration of `func_1().split()`.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: `ans` is a set of all unique values computed from `(q + r) % n` and `(q - r) % n` for each `q` in the previous `ans` set, based on the `c` values from each iteration. If `0` was in `ans`, it is excluded and `n` is added to the set. If `0` was not in `ans`, the set remains unchanged. `n`, `m`, `x`, and `r` remain unchanged; `c` is the value from the last iteration of `func_1().split()`.
    print(len(ans))
    #This is printed: len(ans) (where len(ans) is the number of elements in the set `ans` after the transformation)
    print(*sorted(ans))
    #This is printed: sorted unique values of the `ans` set, where `ans` is computed from `(q + r) % n` and `(q - r) % n` for each `q` in the `ans` set, and if `0` was in the set, it is excluded, and `n` is added
#Overall this is what the function does:The function `func_4` computes a set of unique values based on a series of operations involving addition and subtraction modulo `n`. It starts with an initial value `x` and iteratively updates this set `m` times by adding or subtracting `r` modulo `n`, depending on the character `c` which can be '0', '1', or '?'. If the result of these operations includes `0`, it is replaced with `n`. The function then prints the number of elements in the final set and the sorted elements themselves.

