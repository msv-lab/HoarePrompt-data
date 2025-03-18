#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where [a], [b], [c], and [d] are integers such that 0 <= a, b, c, d < n, and n is the length of the permutation p)
    sys.stdout.flush()
    return input().strip()
    #The program returns the input string after stripping any leading and trailing whitespace.
#Overall this is what the function does:The function `func_1` accepts four integer parameters `a`, `b`, `c`, and `d`, prints a query string in the format `? a b c d` to the console, and then returns the user's input string after removing any leading and trailing whitespace. The function does not modify the input parameters or any other state outside of its scope.

#State of the program right berfore the function call: a and b are integers such that 0 <= a < n and 0 <= b < n, where n is the length of the permutation p.
def func_2(a, b):
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where a and b are integers such that 0 <= a < n and 0 <= b < n, and n is the length of the permutation p)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts two integers `a` and `b` within the bounds of a permutation `p` (0 <= a < n and 0 <= b < n, where n is the length of `p`). It prints a formatted string `! [a] [b]` to the standard output and flushes the output buffer. The function does not return any value. After the function concludes, the formatted string has been printed, and the output buffer has been flushed.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_3():
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program returns None.
    #State: *`n` is an input integer such that 2 <= n <= 10^4, and `n` is not equal to 2
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
        
    #State: `max_index` is `n-1`, `min_indices` is a list containing the indices of all elements in the range `[0, n-1]` that are equal to the element at index `n-1` in the array being compared by `func_1`, or `[0]` if all elements are less than the element at index `n-1`.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: `max_index` is `n-1`, `min_indices` is a list containing the indices of all elements in the range `[0, n-1]` that are equal to the element at index `n-1` in the array being compared by `func_1`, or `[0]` if all elements are less than the element at index `n-1`, `min_index` is the last element of `min_indices` that is not equal to `max_index`, or `max_index` if no such element exists.
    func_2(max_index, min_index)
#Overall this is what the function does:The function `func_3` does not accept any parameters and always returns `None`. It reads an integer `n` from the user input, where `2 <= n <= 10^4`. If `n` is 2, it calls `func_2(0, 1)` and returns. Otherwise, it determines the index of the maximum element (`max_index`) and the index of the minimum element (`min_index`) in a sequence of `n` elements, which are compared using `func_1`. The function then calls `func_2(max_index, min_index)`. The final state of the program is that `max_index` is the index of the maximum element, and `min_index` is the index of the minimum element among the elements that are equal to or less than the element at `max_index`.

