#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the secret permutation p.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are integers such that 0 <= a, b, c, d < n)
    return input()
    #The program returns the input provided to the program.
#Overall this is what the function does:The function `func_1` takes four integer parameters `a`, `b`, `c`, and `d`, each within the range from 0 to `n-1`, where `n` is the length of a secret permutation `p`. It prints a formatted request string containing these integers and then returns the input received from the user.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: `max_item_idx` is the largest `i` (from 1 to `n-1`) for which `func_1(max_item_idx, max_item_idx, i, i)` returns '<'.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: `max_item_idx` is the largest `i` (from 1 to `n-1`) for which `func_1(max_item_idx, max_item_idx, i, i)` returns '<', and `pair_idx` is the largest `i` (from 0 to `n-1`) such that `func_1(max_item_idx, pair_idx, max_item_idx, i)` returns '<' or `func_1(max_item_idx, pair_idx, max_item_idx, i)` returns '=' and `func_1(pair_idx, pair_idx, i, i)` returns '>'.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx] (where max_item_idx is the largest index i from 1 to n-1 such that func_1(max_item_idx, max_item_idx, i, i) returns '<', and pair_idx is the largest index i from 0 to n-1 such that func_1(max_item_idx, pair_idx, max_item_idx, i) returns '<' or func_1(max_item_idx, pair_idx, max_item_idx, i) returns '=' and func_1(pair_idx, pair_idx, i, i) returns '>')
#Overall this is what the function does:The function `func_2` accepts an integer `n` such that 2 <= n <= 10^4. It determines two indices, `max_item_idx` and `pair_idx`, based on the results of comparisons performed by the function `func_1`. It prints these indices in the format `! [max_item_idx] [pair_idx]`.

