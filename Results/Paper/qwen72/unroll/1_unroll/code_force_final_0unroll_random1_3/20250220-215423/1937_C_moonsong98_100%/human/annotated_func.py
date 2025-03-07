#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where [a], [b], [c], and [d] are integers such that 0 <= a, b, c, d < n, and n is the length of the permutation p)
    sys.stdout.flush()
    return input().strip()
    #The program returns the input provided by the user, stripped of leading and trailing whitespace.
#Overall this is what the function does:The function `func_1` accepts four integer parameters `a`, `b`, `c`, and `d`, and prints a query in the format `? [a] [b] [c] [d]` to the standard output. After printing, it flushes the standard output buffer and then reads a line of input from the user, returning this input stripped of any leading and trailing whitespace. The function does not modify the input parameters `a`, `b`, `c`, and `d`, and the final state of the program includes the printed query and the returned user input.

#State of the program right berfore the function call: a and b are non-negative integers such that 0 <= a, b < n, where n is the size of the permutation p.
def func_2(a, b):
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where a and b are non-negative integers such that 0 <= a, b < n, and n is the size of the permutation p)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts two parameters `a` and `b`, which are non-negative integers less than the size of the permutation `p`. It prints the string `! [a] [b]` to the standard output, where `[a]` and `[b]` are the values of `a` and `b` respectively. The function does not return any value. After the function concludes, the values of `a` and `b` remain unchanged, and the permutation `p` is not modified.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_3():
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program returns None.
    #State: `n` is an input integer such that 2 <= n <= 10^4, and `n` is not equal to 2.
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
        
    #State: `max_index` is `n-1`, `min_indices` is a list containing all indices `i` where `func_1(max_index, min_indices[0], max_index, i)` returns `'='` or the smallest index `i` where `func_1(max_index, min_indices[0], max_index, i)` returns `'<'`.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: `max_index` remains `n-1`, `min_indices` remains unchanged, `min_index` is the last index in `min_indices` that is not equal to `max_index` and for which `func_1(min_index, min_index, min_index, i)` returns `'='`. If no such index exists, `min_index` remains `min_indices[0]`.
    func_2(max_index, min_index)
#Overall this is what the function does:The function `func_3` reads an integer `n` from the user input, where `2 <= n <= 10^4`. It then determines the maximum and minimum indices based on the results of calls to `func_1`. Finally, it calls `func_2` with the maximum index and the minimum index (which is not equal to the maximum index, if such an index exists). The function does not return any value; it returns `None`.

