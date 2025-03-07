#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: '? a b c d'
    return input()
    #The program returns a string input requested from the user starting with '?' followed by the integers a, b, c, d
#Overall this is what the function does:The function `func_1` accepts four integer parameters `a`, `b`, `c`, and `d`, each in the range [0, n), and returns a string input from the user. This returned string starts with a question mark (`?`) followed by the values of `a`, `b`, `c`, and `d` in the same order.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: max_item_idx is 3.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: max_item_idx is 3, pair_idx is 2.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! 3 2
#Overall this is what the function does:The function accepts an integer `n` where 2 ≤ n ≤ 10^4, and determines two indices, `max_item_idx` and `pair_idx`, based on comparisons using `func_1`. It then prints these indices in the format `! max_item_idx pair_idx`. The final output is `! 3 2`.

