#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: '? a b c d' (where a, b, c, and d are non-negative integers with their initial values)
    return input()
    #The program returns the string '? a b c d' where 'a', 'b', 'c', and 'd' are the same as their initial values.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d`. It prints a request string `'? a b c d'` and then waits for user input, returning the same request string back to the caller. The returned string includes the original values of `a`, `b`, `c`, and `d`.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: Output State: `max_item_idx` is the index `i` for which `func_1(max_item_idx, max_item_idx, i, i)` returns '<', or 0 if no such `i` exists within the range 1 to n-1.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: Output State: `pair_idx` is the index `i` for which `func_1(max_item_idx, max_item_idx, i, i)` returns '<' and `func_1(pair_idx, pair_idx, i, i)` returns '>', or `max_item_idx` if no such `i` exists within the range 1 to n-1. If no such `i` exists, then `pair_idx` remains equal to `max_item_idx`.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx]
#Overall this is what the function does:The function `func_2` accepts an integer `n` (where 2 ≤ n ≤ 10^4) and processes it to find two indices, `max_item_idx` and `pair_idx`. It first determines `max_item_idx` by comparing values using `func_1` and then finds `pair_idx` by further comparisons. Finally, it prints the values of `max_item_idx` and `pair_idx` in the format `! [max_item_idx] [pair_idx]`. If no suitable indices are found, `max_item_idx` and `pair_idx` remain unchanged.

