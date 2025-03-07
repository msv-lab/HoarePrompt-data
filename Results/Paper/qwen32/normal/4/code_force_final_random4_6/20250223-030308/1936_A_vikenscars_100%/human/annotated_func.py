#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? a b c d (where a, b, c, and d are integers such that 0 <= a, b, c, d < n)
    return input()
    #The program returns the value of the input() function, which is a string formatted as '? a b c d' where a, b, c, and d are integers such that 0 <= a, b, c, d < n, and n is the length of the permutation p.
#Overall this is what the function does:The function takes four integer parameters `a`, `b`, `c`, and `d`, each within the range 0 to n-1, where n is the length of a permutation `p`. It prints a formatted string `? a b c d` and returns the value of the subsequent input, which is expected to be a string in the same format.

#State of the program right berfore the function call: n is an integer representing the length of the permutation sequence, where 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: `max_item_idx` is the largest index `i` (from 1 to `n-1`) for which `func_1(max_item_idx, max_item_idx, i, i)` returns `'<'`. If no such `i` exists, `max_item_idx` is 0.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: `max_item_idx` is the largest index `i` (from 1 to `n-1`) for which `func_1(max_item_idx, max_item_idx, i, i)` returns `'<'`. `pair_idx` is the index of the item that is greater than all other items when compared using `func_1`.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx] (where max_item_idx is the largest index i (from 1 to n-1) for which func_1(max_item_idx, max_item_idx, i, i) returns '<', and pair_idx is the index of the item that is greater than all other items when compared using func_1)
#Overall this is what the function does:The function `func_2` accepts an integer `n` representing the length of a permutation sequence. It determines and prints two indices: the largest index `max_item_idx` for which a specific comparison function `func_1` returns `'<'` when comparing it with itself, and another index `pair_idx` which is the index of the item that is greater than all other items according to the comparison function `func_1`.

