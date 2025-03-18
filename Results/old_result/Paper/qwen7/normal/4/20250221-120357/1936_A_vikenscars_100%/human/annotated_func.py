#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: '? [a] [b] [c] [d]' (where [a], [b], [c], and [d] are the respective values of the variables a, b, c, and d)
    return input()
    #The program returns a string entered by the user that matches the format '? {a} {b} {c} {d}', where 'a', 'b', 'c', and 'd' are the initial non-negative integer values provided.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d`. It formats these parameters into a string and prints it to the console. The function then waits for the user to enter a string that matches the printed format and returns the entered string.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: The loop will execute from i=1 to i=n-1. After all iterations, max_item_idx will be n-1 if func_1(max_item_idx, max_item_idx, i, i) returns '<' for each i from 1 to n-1. Otherwise, max_item_idx will remain 0.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: Output State: After the loop executes all iterations, `max_item_idx` remains 0, `pair_idx` is set to the last index `i` which is `n-1`, and `i` is equal to `n-1`. The value of `ans1` is the return value of `func_1(0, n-1, 0, n-1)`. If `ans1` equals `'<'`, then `ans1` is `'<'`. If `ans1` equals `'='` and `ans2` (the return value of `func_1(n-1, n-1, n-1, n-1)`) equals `'>'`, then `ans1` remains `'='`. Otherwise, `ans1` is `'='`.
    #
    #This means that after all iterations, `pair_idx` will hold the index of the last element processed, and the final state of `ans1` will depend on the comparison results from the function calls within the loop.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! 0 n-1
#Overall this is what the function does:The function accepts an integer `n` between 2 and 10^4 inclusive. It iterates through indices to find the last index `pair_idx` based on certain conditions involving the `func_1` function. Finally, it prints `! 0 n-1` and returns `None`. If `n` is outside the specified range, it does not perform any action other than the iteration and printing.

