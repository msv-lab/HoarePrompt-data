#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: '? a b c d' (where a, b, c, and d are the same non-negative integers as specified in the request string)
    return input()
    #The program returns the string '? a b c d' where 'a', 'b', 'c', and 'd' are the same non-negative integers as before.
#Overall this is what the function does:The function accepts four non-negative integer parameters \(a\), \(b\), \(c\), and \(d\). It constructs and prints a request string in the format '? a b c d'. The function then waits for user input and returns the same request string as a response.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: Output State: `max_item_idx` is the index `i` for which the condition `func_1(i, i, max_item_idx, max_item_idx) == '<'` holds true, or remains 0 if no such index exists.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: Output State: `pair_idx` is the index `i` for which `func_1(max_item_idx, max_item_idx, max_item_idx, i)` returns '<', or `func_1(pair_idx, pair_idx, i, i)` returns '>' if no such `i` satisfies the first condition, or remains 0 if no such index exists.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx]
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 10^4) and determines two indices, `max_item_idx` and `pair_idx`, based on comparisons using `func_1`. It then prints these indices in the format "! [max_item_idx] [pair_idx]". The function does not return any value; its output is the printed result.

