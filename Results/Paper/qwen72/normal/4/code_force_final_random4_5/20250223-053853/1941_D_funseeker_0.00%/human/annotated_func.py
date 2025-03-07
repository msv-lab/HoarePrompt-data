#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_1():
    return sys.stdin.readline().strip()
    #The program returns the first line of input from the standard input (stdin), with any trailing whitespace removed.
#Overall this is what the function does:The function `func_1` reads the first line of input from the standard input (stdin) and returns this line with any trailing whitespace removed. The function does not take any parameters and does not modify any external state. After the function concludes, the program has read one line from stdin and the returned value is the stripped version of that line.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 1000, m is an integer such that 1 <= m <= 1000, x is an integer such that 1 <= x <= n, and throws is a list of tuples where each tuple contains an integer r_i (1 <= r_i <= n - 1) and a string c_i ('0', '1', or '?').
def func_2():
    return int(func_1())
    #The program returns an integer value that is the result of the function `func_1()`. The specific value of the integer depends on the implementation of `func_1()` and the initial values of `n`, `m`, `x`, and `throws`.
#Overall this is what the function does:The function `func_2` accepts parameters `n`, `m`, `x`, and `throws`. It returns an integer value that is the result of calling `func_1()`. The specific integer value depends on the implementation of `func_1()` and the initial values of `n`, `m`, `x`, and `throws`. After the function concludes, the state of the program includes the returned integer value, and the original parameters `n`, `m`, `x`, and `throws` remain unchanged.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_3():
    return list(map(int, func_1().split()))
    #The program returns a list of integers obtained by splitting the string returned from `func_1()` and converting each part to an integer.
#Overall this is what the function does:The function `func_3` does not accept any parameters and returns a list of integers. This list is obtained by splitting the string returned from `func_1()` and converting each part to an integer.

#State of the program right berfore the function call: n, m, x are integers such that 2 <= n <= 1000, 1 <= m <= 1000, and 1 <= x <= n.
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
        
    #State: `n`, `m`, and `x` remain unchanged, and `ans` is a set containing all possible values of `(x + k*r) % n` and `(x - k*r) % n` for all integers `k` from `0` to `m`, where `r` and `c` are the values returned by `func_1()` in each iteration.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: *`n`, `m`, and `x` remain unchanged, and `ans` is a set containing all possible values of `(x + k*r) % n` and `(x - k*r) % n` for all integers `k` from `0` to `m`, where `r` and `c` are the values returned by `func_1()` in each iteration. If `0` is in `ans`, then `0` is removed from the set and `n` is added to the set. Otherwise, `ans` remains unchanged.
    print(len(ans))
    #This is printed: len(ans) (where `ans` is the set containing all possible values of `(x + k*r) % n` and `(x - k*r) % n` for `k` from `0` to `m`, with `0` removed and `n` added if `0` is present)
    print(*ans)
    #This is printed: [elements of ans] (where ans is a set containing all unique values of (x + k*r) % n and (x - k*r) % n for k from 0 to m, with 0 replaced by n if 0 is present)
#Overall this is what the function does:The function `func_4` accepts no parameters but uses the integers `n`, `m`, and `x` (where `2 <= n <= 1000`, `1 <= m <= 1000`, and `1 <= x <= n`) provided by the function `func_3`. It computes a set `ans` containing all possible values of `(x + k*r) % n` and `(x - k*r) % n` for all integers `k` from `0` to `m`, where `r` and `c` are values returned by `func_1()` in each iteration. If `0` is in the set `ans`, it is removed and `n` is added to the set. The function then prints the length of the set `ans` and the elements of the set `ans`.

