#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n.
def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    #This is printed: '? [a] [b] [c] [d]' (where [a], [b], [c], and [d] are non-negative integers such that 0 <= [a], [b], [c], [d] < n)
    sys.stdout.flush()
    return input().strip()
    #The program returns an input value after stripping whitespace.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d`, each less than `n`. It prints these parameters and then waits for user input, returning the input value after removing any leading or trailing whitespace.

#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n.
def func_2(a, b):
    print(f'! {a} {b}')
    #This is printed: ! [a] [b]
    sys.stdout.flush()
#Overall this is what the function does:The function accepts two integer parameters `a` and `b`. It prints the values of `a` and `b` in a formatted string and flushes the output buffer. The function does not modify the input parameters and returns no value.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_3():
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program does not return any value since there is no return statement in the provided code.
    #State: `n` is an input integer within the range 2 to 10^4, and `n` is not equal to 2
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: After all iterations of the loop, `max_index` will be equal to `n-1` if for every `i` from 0 to `n-1`, `func_1(0, max_index, 0, i)` returns '<'. Otherwise, `max_index` will be the largest `i` such that `func_1(0, max_index, 0, i)` returns '<'.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        else:
            min_indices.append(i)
        
    #State: Output State: `min_indices` is a list that contains either `max_index` and all integers from `0` to `n-1` if `res` was not `'<'` in any iteration, or just the last integer `n-1` if `res` was `'<'` in all iterations.
    #
    #To break this down further:
    #- The loop runs `n` times, iterating over each index from `0` to `n-1`.
    #- In each iteration, `res` is determined by calling `func_1(max_index, min_indices[0], max_index, i)`.
    #- If `res` is `<`, `min_indices` is reset to contain only the current index `i`.
    #- If `res` is not `<`, the current index `i` is appended to `min_indices`.
    #
    #After all iterations, `min_indices` will either contain a single element `n-1` if `res` was always `<`, or it will contain `max_index` followed by all integers from `0` to `n-1` if `res` was not `<` in any iteration.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: min_index is the last element in min_indices.
    func_2(max_index, min_index)
#Overall this is what the function does:The function processes an integer `n` (where 2 ≤ n ≤ 10^4) by calling `func_1` and `func_2`. It first determines a `max_index` based on the results of `func_1` calls, then constructs a list `min_indices` based on these results. Finally, it updates `min_index` based on the values in `min_indices` and calls `func_2` with `max_index` and `min_index` as arguments. The function does not return any value.

