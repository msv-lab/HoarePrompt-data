#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: "? {a} {b} {c} {d}" (where {a}, {b}, {c}, and {d} are the actual values of the integers a, b, c, and d, respectively, and 0 <= a, b, c, d < n)
    return input()
    #The program returns the user input, which is expected to be a string formatted as `"? {a} {b} {c} {d}"`, where `a`, `b`, `c`, and `d` are integers such that 0 <= a, b, c, d < n, and `n` is the length of the permutation `p`.
#Overall this is what the function does:The function `func_1` accepts four integers `a`, `b`, `c`, and `d` such that 0 <= a, b, c, d < n, where `n` is the length of the permutation `p`. It prints a query string formatted as `"? {a} {b} {c} {d}"` to the console and then returns the user's input as a string. The user's input is expected to be a string formatted similarly, but the function does not enforce this format.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: `max_item_idx` is the index of the largest item in the range 1 to n-1, assuming `func_1` returns '<' when the item at index `i` is larger than the item at `max_item_idx`.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: `pair_idx` is the index of the largest item in the range 0 to n-1.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx] (where `max_item_idx` is the value of the undefined variable `max_item_idx` and `pair_idx` is the index of the largest item in the range 0 to n-1)
#Overall this is what the function does:The function `func_2` accepts an integer `n` where 2 ≤ n ≤ 10^4. It determines the index of the largest item in the range 0 to n-1 using a comparison function `func_1`. After the function concludes, it prints the indices of two items: `max_item_idx` and `pair_idx`. `max_item_idx` is the index of the largest item found in the range 1 to n-1, and `pair_idx` is the index of the largest item in the range 0 to n-1. The final state of the program includes the printed output in the format `! [max_item_idx] [pair_idx]`.

