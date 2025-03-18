#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 <= a, b, c, d < n.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: '? [a] [b] [c] [d]' (where [a], [b], [c], and [d] are the values of the variables a, b, c, and d respectively)
    return input()
    #The program returns a string entered by the user that matches the format '? {a} {b} {c} {d}', where 'a', 'b', 'c', and 'd' are the initial non-negative integer values provided.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `a`, `b`, `c`, and `d`. It prints a request string formatted as `'? {a} {b} {c} {d}'` and then waits for the user to enter a matching string. The function returns the string entered by the user.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: max_item_idx is 3, n is greater than 1 and less than or equal to 10^4.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: max_item_idx is 3, pair_idx is 2, i is 3, ans1 is the return value of func_1(3, 2, 3, 3), and ans2 is the return value of func_1(2, 2, 2, 2).
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! 3 2
#Overall this is what the function does:The function accepts an integer `n` within the range 2 to 10^4 (inclusive). It then finds two indices, `max_item_idx` and `pair_idx`, by comparing values using `func_1`. After determining these indices, it prints them in the format `! max_item_idx pair_idx`. If `n` is outside the specified range, no action is performed and the function ends.

