#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where [a], [b], [c], and [d] are non-negative integers less than n)
    sys.stdout.flush()
    return input().strip()
    #The program returns the input string after stripping leading and trailing whitespace.
#Overall this is what the function does:The function `func_1` accepts four parameters `a`, `b`, `c`, and `d`, which are non-negative integers. It prints a query string in the format `? [a] [b] [c] [d]` and then returns the input string provided by the user after stripping any leading and trailing whitespace.

#State of the program right berfore the function call: a and b are integers such that 0 <= a < n and 0 <= b < n, where n is the length of the permutation p.
def func_2(a, b):
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where [a] and [b] are integers such that 0 <= a < n and 0 <= b < n, and n is the length of the permutation p)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts two parameters `a` and `b`, both integers within the range of a permutation `p` (0 to n-1, where n is the length of `p`). It prints the string `! [a] [b]` to the standard output, where `[a]` and `[b]` are the integer values of `a` and `b`. The function does not return any value. After the function concludes, the standard output will contain the printed string, and the state of the program remains unchanged except for the side effect of the print operation.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_3():
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program returns nothing.
    #State: *`n` is an input integer, 2 <= n <= 10^4, and `n` is not equal to 2
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: `max_index` is `n-1`.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: `max_index` is `n-1`, `min_indices` is a list containing all indices `i` where `func_1(max_index, min_indices[0], max_index, i)` returns `'='`, and the smallest index `i` where `func_1(max_index, min_indices[0], max_index, i)` returns `'<'`. If no such index exists, `min_indices` will contain all indices from `0` to `n-1`.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: `min_index` is the last index in `min_indices` that is not equal to `max_index`. If all indices in `min_indices` are equal to `max_index`, `min_index` remains unchanged.
    func_2(max_index, min_index)
#Overall this is what the function does:The function `func_3` reads an integer `n` from the user input, where `2 <= n <= 10^4`. It then determines the maximum and minimum indices based on the results of `func_1` comparisons. Finally, it calls `func_2` with the maximum index and the minimum index (which is the last index in the list of minimum indices that is not equal to the maximum index, or the first index in the list if all are equal to the maximum index). The function does not accept any parameters and returns nothing.

