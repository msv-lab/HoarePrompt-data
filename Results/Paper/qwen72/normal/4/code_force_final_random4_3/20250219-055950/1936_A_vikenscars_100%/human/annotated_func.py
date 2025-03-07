#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? {a} {b} {c} {d} (where {a}, {b}, {c}, and {d} are the specific values of a, b, c, and d respectively)
    return input()
    #The program returns the string `'? {a} {b} {c} {d}'`, where `{a}`, `{b}`, `{c}`, and `{d}` are the specific values of `a`, `b`, `c`, and `d` respectively.
#Overall this is what the function does:The function `func_1` accepts four integer parameters `a`, `b`, `c`, and `d` within the range 0 to n-1, where `n` is the length of a permutation `p`. It prints a formatted query string `'? {a} {b} {c} {d}'` to the standard output and then reads a line of input from the standard input, returning it as a string. The final state of the program after the function concludes is that the input string, which is the response to the printed query, is returned.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: `n` is an integer such that 2 <= n <= 10^4, `i` is `n-1`, `max_item_idx` is the index of the last `i` for which `func_1(max_item_idx, max_item_idx, i, i)` returned '<'. If `func_1` never returned '<', `max_item_idx` remains 0.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: `n` is an integer such that 2 <= n <= 10^4, `i` is `n-1`, `max_item_idx` is the index of the last `i` for which `func_1(max_item_idx, max_item_idx, i, i)` returned '<'. If `func_1` never returned '<', `max_item_idx` remains 0. `pair_idx` is the index of the last `i` for which `func_1(max_item_idx, pair_idx, max_item_idx, i)` returned '<' or the last `i` for which `func_1(pair_idx, pair_idx, i, i)` returned '>'. If no such `i` exists, `pair_idx` remains equal to `max_item_idx`.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! {max_item_idx} {pair_idx} (where max_item_idx is the last index for which func_1(max_item_idx, max_item_idx, i, i) returned '<' or 0 if no such index exists, and pair_idx is the last index for which func_1(max_item_idx, pair_idx, max_item_idx, i) returned '<' or func_1(pair_idx, pair_idx, i, i) returned '>', or equal to max_item_idx if no such index exists)
#Overall this is what the function does:The function `func_2` accepts an integer `n` such that 2 <= n <= 10^4. It determines two indices, `max_item_idx` and `pair_idx`, based on the results of calls to `func_1`. Specifically, `max_item_idx` is the index of the last `i` for which `func_1(max_item_idx, max_item_idx, i, i)` returned '<', or 0 if no such `i` exists. `pair_idx` is the index of the last `i` for which `func_1(max_item_idx, pair_idx, max_item_idx, i)` returned '<' or the last `i` for which `func_1(pair_idx, pair_idx, i, i)` returned '>', or equal to `max_item_idx` if no such `i` exists. The function then prints the result in the format `! {max_item_idx} {pair_idx}`.

