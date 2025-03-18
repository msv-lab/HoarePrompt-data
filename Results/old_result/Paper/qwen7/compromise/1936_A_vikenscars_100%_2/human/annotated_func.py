#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: '? a b c d'
    return input()
    #The program returns a string input requested from the user starting with '?' followed by the values of 'a', 'b', 'c', and 'd'
#Overall this is what the function does:The function `func_1` accepts four integer parameters `a`, `b`, `c`, and `d`, each within the range [0, n). It prints a request string starting with '?' followed by the values of `a`, `b`, `c`, and `d`. The function then waits for and returns a string input from the user, which must start with '?' followed by the same values of `a`, `b`, `c`, and `d`.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: Output State: `max_item_idx` is the index `i` for which `func_1(max_item_idx, max_item_idx, i, i)` returns '<' for the first time, or 0 if no such `i` exists within the range 1 to `n-1`.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: pair_idx is equal to the index `i` that makes `ans1` equal to '<' or, if no such `i` exists, it remains equal to `max_item_idx`.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx]
#Overall this is what the function does:Functionality: The function accepts an integer `n` within the range of 2 to \(10^4\). It iterates through indices from 1 to `n-1` to find an index `max_item_idx` for which `func_1(max_item_idx, max_item_idx, i, i)` returns '<'. If no such index exists, `max_item_idx` remains 0. Then, it further iterates through all indices from 0 to `n-1` to find an index `pair_idx` such that `func_1(max_item_idx, pair_idx, max_item_idx, i)` returns '<' or, if that condition is not met, `func_1(pair_idx, pair_idx, i, i)` returns '>'. Finally, it prints the values of `max_item_idx` and `pair_idx`.

