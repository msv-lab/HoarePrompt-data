#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: '? {a} {b} {c} {d}' (where {a}, {b}, {c}, and {d} are the specific values of a, b, c, and d, respectively, and 0 <= a, b, c, d < n)
    return input()
    #The program returns the string 'request' which is formatted as '? {a} {b} {c} {d}', where {a}, {b}, {c}, and {d} are the specific values of a, b, c, and d, respectively.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d`, and prints a formatted string `'? {a} {b} {c} {d}'` to the console. It then returns the user's input as a string. The function does not modify the input parameters or any other state in the program.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: `n` is an integer such that 2 <= n <= 10^4, `i` is `n-1`, and `max_item_idx` is the index `i` for which `func_1(max_item_idx, max_item_idx, i, i)` returned '<' for the last time, or 0 if `func_1` never returned '<' during the loop execution.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: `n` is an integer such that 2 <= n <= 10^4, `i` is `n-1`, `max_item_idx` is the index `i` for which `func_1(max_item_idx, max_item_idx, i, i)` returned '<' for the last time, or 0 if `func_1` never returned '<' during the loop execution, `pair_idx` is the index `i` for which `func_1(max_item_idx, pair_idx, max_item_idx, i)` returned '<' for the last time, or the last index `i` for which `func_1(pair_idx, pair_idx, i, i)` returned '>' if `ans1` was '='.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx] (where `max_item_idx` is the index `i` for which `func_1(max_item_idx, max_item_idx, i, i)` returned '<' for the last time, or 0 if `func_1` never returned '<' during the loop execution, and `pair_idx` is the index `i` for which `func_1(max_item_idx, pair_idx, max_item_idx, i)` returned '<' for the last time, or the last index `i` for which `func_1(pair_idx, pair_idx, i, i)` returned '>' if `ans1` was '=')
#Overall this is what the function does:The function `func_2` accepts an integer `n` where 2 <= n <= 10^4. It determines two indices, `max_item_idx` and `pair_idx`, based on the results of calls to `func_1`. The `max_item_idx` is the index `i` for which `func_1(max_item_idx, max_item_idx, i, i)` returned '<' for the last time during the first loop, or 0 if `func_1` never returned '<'. The `pair_idx` is the index `i` for which `func_1(max_item_idx, pair_idx, max_item_idx, i)` returned '<' for the last time during the second loop, or the last index `i` for which `func_1(pair_idx, pair_idx, i, i)` returned '>' if `ans1` was '='. The function then prints the result in the format `! [max_item_idx] [pair_idx]`. The function does not return any value.

