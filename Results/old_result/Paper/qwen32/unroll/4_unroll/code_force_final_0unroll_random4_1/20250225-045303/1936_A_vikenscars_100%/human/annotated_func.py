#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n, where n is the length of the secret permutation p.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n)
    return input()
    #The program returns the value provided by the user input.
#Overall this is what the function does:The function `func_1` takes four non-negative integer parameters `a`, `b`, `c`, and `d`, each less than `n`, where `n` is the length of a secret permutation `p`. It prints a formatted request string containing these parameters and returns the value provided by the user input.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation sequence, where 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: `n` is a positive integer representing the length of the permutation sequence, where 2 <= n <= 10^4; `max_item_idx` is n-1
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: n is a positive integer representing the length of the permutation sequence, where 2 <= n <= 10^4; max_item_idx is n-1; pair_idx is the index of the smallest element in the permutation sequence.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [n-1] [pair_idx] (where [n-1] is n-1 and [pair_idx] is the index of the smallest element in the permutation sequence)
#Overall this is what the function does:The function `func_2` accepts a positive integer `n` representing the length of a permutation sequence, where 2 <= n <= 10^4. It determines the index of the largest element (`max_item_idx`) and the index of the smallest element (`pair_idx`) in the permutation sequence. The function then prints these indices in the format `! [n-1] [pair_idx]`.

