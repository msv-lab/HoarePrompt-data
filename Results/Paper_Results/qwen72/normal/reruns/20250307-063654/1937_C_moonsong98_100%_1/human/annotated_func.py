#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where [a], [b], [c], and [d] are integers such that 0 <= [a], [b], [c], [d] < n, and n is the length of the permutation p)
    sys.stdout.flush()
    return input().strip()
    #The program returns the input string after stripping leading and trailing whitespace.
#Overall this is what the function does:The function `func_1` takes four integer parameters `a`, `b`, `c`, and `d`, which are expected to be within the range 0 to `n-1` (inclusive), where `n` is the length of a permutation `p`. It prints a query string in the format `? a b c d` and then returns the user's input after stripping any leading and trailing whitespace. The function does not modify the input parameters or any external state.

#State of the program right berfore the function call: a and b are integers such that 0 <= a < n and 0 <= b < n, where n is the length of the permutation p.
def func_2(a, b):
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where [a] and [b] are integers such that 0 <= a < n and 0 <= b < n, and n is the length of the permutation p)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts two parameters `a` and `b`, both of which are integers within the range [0, n-1) where `n` is the length of the permutation `p`. It prints the string `! [a] [b]` to the standard output, where `[a]` and `[b]` are the integer values of `a` and `b`. The function does not return any value. After the function concludes, the state of the program remains unchanged except for the output that has been printed.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_3():
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program returns nothing.
    #State: *`n` is an integer provided by the user, and it is within the range 2 <= n <= 10^4. Additionally, `n` is not equal to 2.
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: After the loop executes all the iterations, `i` is `n-1`, `n` remains an integer within the range 2 <= n <= 10^4 and not equal to 2, `max_index` is the last index `i` for which `func_1(0, max_index, 0, i)` returned '<', and `res` is the result of `func_1(0, max_index, 0, n-1)`.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: `i` is `n-1`, `n` remains an integer within the range 2 <= n <= 10^4 and not equal to 2, `max_index` is the last index `i` for which `func_1(0, max_index, 0, i)` returned '<', `res` is the result of `func_1(max_index, min_indices[0], max_index, n-1)`, `min_indices` is a list containing the indices `i` for which `func_1(max_index, min_indices[0], max_index, i)` returned '<' or '='.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: `i` has iterated through all elements in `min_indices`, `n` remains an integer within the range 2 <= n <= 10^4 and not equal to 2, `max_index` is the last index `i` for which `func_1(0, max_index, 0, i)` returned '<', `res` is the result of the last `func_1(min_index, min_index, min_index, i)` call, and `min_index` is the last index `i` in `min_indices` for which `func_1(min_index, min_index, min_index, i)` returned '='.
    func_2(max_index, min_index)
#Overall this is what the function does:The function `func_3` reads an integer `n` from the user input, where `2 <= n <= 10^4`. If `n` is 2, it calls `func_2(0, 1)` and returns immediately. Otherwise, it determines the maximum index `max_index` for which `func_1(0, max_index, 0, i)` returns '<' for all `i` in the range `[0, n)`. It then identifies all indices `min_indices` for which `func_1(max_index, min_indices[0], max_index, i)` returns '<' or '='. Finally, it selects the last index `min_index` from `min_indices` that satisfies `func_1(min_index, min_index, min_index, i) == '='` and calls `func_2(max_index, min_index)`. The function does not return any value.

