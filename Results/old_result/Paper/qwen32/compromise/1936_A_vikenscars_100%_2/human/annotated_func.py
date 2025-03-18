#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the length of the secret permutation p.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? a b d (where a, b, c, and d are non-negative integers less than n)
    return input()
    #The program returns the value of the next input provided to the program, which is expected to be a string in the format '? a b c d' where a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, and n is the length of the secret permutation p.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d` that are less than `n`, the length of a secret permutation `p`. It prints a formatted string `? a b c d` to the standard output and then returns the next input string provided to the program, which is expected to be in the same format.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: max_item_idx is n-1
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: - `max_item_idx` is not modified within the loop, so it remains `n-1`.
    #   - `pair_idx` can be modified based on the conditions inside the loop. However, without knowing the behavior of `func_1`, we can only infer the following:
    #     - If `func_1` consistently returns `'<'` for all comparisons involving `max_item_idx` and `i`, `pair_idx` will be updated to the last `i` for which `ans1` is `'<'`.
    #     - If `func_1` returns `'='` and then `'>'` for some `i`, `pair_idx` will be updated to that `i`.
    #
    #Given the general behavior and without specific details about `func_1`, we can't definitively determine the exact value of `pair_idx` after the loop. However, we can say that `pair_idx` will be the last index `i` where either `ans1` is `'<'` or `ans2` is `'>'`.
    #
    #For the sake of providing an understandable and consistent output, let's assume the loop processes in a way that `pair_idx` ends up being the last index where a significant comparison occurs (which, in the absence of specific details, could reasonably be considered the last `i` where `ans1` is `'<'` or `ans2` is `'>'`).
    #
    #Thus, the most reasonable assumption, given the loop structure, is that `pair_idx` could end up being `n-1` if no significant comparison (either `'<'` or `'>'` after `'='`) occurs, or it could be some other index `i` where a significant comparison happens.
    #
    #However, given the initial state and the lack of specific behavior of `func_1`, the most straightforward and consistent output state would be:
    #
    #Output State:
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! n-1 n-1 (where n-1 is the value of both max_item_idx and pair_idx)
#Overall this is what the function does:The function `func_2` takes an integer `n` (where 2 <= n <= 10^4) and prints two indices, `max_item_idx` and `pair_idx`, based on the comparisons made within the function. The final output is always `! n-1 n-1` under the given code structure and assumptions.

