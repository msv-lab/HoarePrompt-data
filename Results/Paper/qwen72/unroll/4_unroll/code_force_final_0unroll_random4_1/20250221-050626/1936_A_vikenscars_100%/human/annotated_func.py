#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? a b c d (where a, b, c, and d are integers such that 0 <= a, b, c, d < n, and n is the length of the permutation p)
    return input()
    #The program returns the string 'request' which is formatted as '? a b c d', where a, b, c, and d are specific integer values from the initial state.
#Overall this is what the function does:The function `func_1` accepts four integer parameters `a`, `b`, `c`, and `d`, all of which are within the range 0 to `n-1` (inclusive), where `n` is the length of a permutation `p`. It prints a formatted query string `? a b c d` to the standard output and then reads a line of input from the standard input. The function returns this input as a string. After the function concludes, the input parameters `a`, `b`, `c`, and `d` remain unchanged, and the program state includes the returned string from the input.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: `max_item_idx` is the index of the last element in the range from 1 to n-1 for which `func_1(max_item_idx, max_item_idx, i, i)` returns '<'. If no such element exists, `max_item_idx` remains 0.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: `max_item_idx` remains the same, and `pair_idx` is the index of the last element in the range from 1 to n-1 for which `func_1(max_item_idx, pair_idx, max_item_idx, i)` returns '<'. If no such element exists, `pair_idx` is the index of the last element in the range from 1 to n-1 for which `func_1(max_item_idx, pair_idx, max_item_idx, i)` returns '=' and `func_1(pair_idx, pair_idx, i, i)` returns '>'. If no such elements exist, `pair_idx` remains 0.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx] (where `max_item_idx` is the fixed value and `pair_idx` is the index determined by the conditions described above)
#Overall this is what the function does:The function `func_2` accepts an integer `n` such that 2 <= n <= 10^4. It determines two indices, `max_item_idx` and `pair_idx`, based on the results of calls to `func_1`. The final state of the program is that `max_item_idx` is the index of the last element in the range from 1 to n-1 for which `func_1(max_item_idx, max_item_idx, i, i)` returns '<'. If no such element exists, `max_item_idx` remains 0. The `pair_idx` is the index of the last element in the range from 1 to n-1 for which `func_1(max_item_idx, pair_idx, max_item_idx, i)` returns '<'. If no such element exists, `pair_idx` is the index of the last element in the range from 1 to n-1 for which `func_1(max_item_idx, pair_idx, max_item_idx, i)` returns '=' and `func_1(pair_idx, pair_idx, i, i)` returns '>'. If no such elements exist, `pair_idx` remains 0. The function then prints the values of `max_item_idx` and `pair_idx` in the format: `! [max_item_idx] [pair_idx]`.

