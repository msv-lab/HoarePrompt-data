#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n.
def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d]
    sys.stdout.flush()
    return input().strip()
    #The program returns a string input by the user after stripping any leading or trailing whitespace.
#Overall this is what the function does:The function `func_1` accepts four integer parameters `a`, `b`, `c`, and `d`, each in the range [0, n). It prints these values and then waits for the user to input a string. After receiving the input, it strips any leading or trailing whitespace and returns the resulting string.

#State of the program right berfore the function call: a, b, c, and d are non-negative integers such that 0 ≤ a, b, c, d < n.
def func_2(a, b):
    print(f'! {a} {b}')
    #This is printed: ! [a] [b]
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts two non-negative integers `a` and `b` such that \(0 \leq a, b < n\), prints them to the console, and does not return any value. After the function concludes, the program state includes the printed values of `a` and `b`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_3():
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program does not return any value
    #State: `n` is an integer equal to the input integer, 2 <= n <= 10^4, and `n` is not equal to 2
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: n is an integer between 2 and 10^4 (inclusive), max_index is the largest value of i for which func_1(0, max_index, 0, i) returns '<', or 0 if no such i exists.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: Output State: `max_index` is the largest value of i for which `func_1(0, max_index, 0, i)` returns '<', or 0 if no such i exists; `min_indices` is a list containing the indices of all i such that `func_1(max_index, min_indices[0], max_index, i)` returns '=' for each i in `min_indices`. Initially, `min_indices` contains only `max_index`.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: `max_index` is the largest value of i for which `func_1(0, max_index, 0, i)` returns '<', or 0 if no such i exists; `min_indices` is a list containing the indices of all i such that `func_1(max_index, min_indices[0], max_index, i)` returns '=' for each i in `min_indices`; `min_index` is the smallest index in `min_indices` that satisfies the condition `func_1(min_index, min_index, min_index, i) == '='` for all i in `min_indices`. If no such index exists, then `min_index` is equal to `max_index`.
    func_2(max_index, min_index)
#Overall this is what the function does:The function reads an integer `n` from the user, where `2 <= n <= 10^4`. It then calls `func_1` and `func_2` to determine two indices, `max_index` and `min_index`, based on certain conditions. Finally, it calls `func_2` with these two indices as arguments. The function does not return any value.

