#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? a b c d (where a, b, c, and d are specific non-negative integers such that 0 <= a, b, c, d < n, and n is the length of the permutation p)
    return input()
    #The program returns the string 'request' which is formatted as '? a b c d', where a, b, c, and d are specific non-negative integers such that 0 <= a, b, c, d < n, and n is the length of the permutation p.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d`, each less than the length of the permutation `p`. It prints a formatted string `? a b c d` to the console and then returns the user's input as a string. The final state of the program is that the formatted string has been printed, and the function has returned the user's input, which can be any string.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: `n` is an integer such that 2 <= n <= 10^4, `max_item_idx` is the highest value of `i` for which `func_1` returned '<' during the loop execution.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: `pair_idx` is the highest value of `i` for which `func_1` returned '<' or the highest value of `i` for which `func_1` returned '=' and `func_1` on the second call returned '>'. `max_item_idx` remains unchanged.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx] (where [max_item_idx] is the unchanged value of `max_item_idx` and [pair_idx] is the highest value of `i` for which `func_1` returned '<' or the highest value of `i` for which `func_1` returned '=' and `func_1` on the second call returned '>')
#Overall this is what the function does:The function `func_2` accepts an integer `n` where 2 <= n <= 10^4. It determines two indices, `max_item_idx` and `pair_idx`, based on the results of calls to `func_1`. The final state of the program after the function concludes is that `max_item_idx` is the highest value of `i` for which `func_1` returned '<' during the first loop, and `pair_idx` is the highest value of `i` for which `func_1` returned '<' or the highest value of `i` for which `func_1` returned '=' and `func_1` on the second call returned '>'. The function then prints the values of `max_item_idx` and `pair_idx` in the format: `! [max_item_idx] [pair_idx]`.

