#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the secret permutation p.
def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    #This is printed: ? [a] [b] [c] [d] (where a, b, c, and d are integers such that 0 <= a, b, c, d < n)
    sys.stdout.flush()
    return input().strip()
    #The program returns the stripped input from the user.
#Overall this is what the function does:The function `func_1` takes four integer parameters `a`, `b`, `c`, and `d`, each within the range from 0 to `n-1`, where `n` is the length of a secret permutation `p`. It prints these four integers in a formatted string, prompts for user input, and returns the stripped version of the input received from the user.

#State of the program right berfore the function call: a and b are integers such that 0 <= a < n and 0 <= b < n, where n is the length of the secret permutation p.
def func_2(a, b):
    print(f'! {a} {b}')
    #This is printed: ! [a] [b] (where a and b are integers such that 0 <= a < n and 0 <= b < n)
    sys.stdout.flush()
#Overall this is what the function does:The function `func_2` accepts two integer parameters `a` and `b`, which are indices within the range of a secret permutation `p`. It prints a formatted string `! [a] [b]` to the standard output, flushes the output buffer, and does not return any value.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^4.
def func_3():
    n = int(input())
    if (n == 2) :
        func_2(0, 1)
        return
        #The program returns None
    #State: `n` is an integer such that 2 <= n <= 10^4, and `n` is not equal to 2
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        
        if res == '<':
            max_index = i
        
    #State: `n` is an integer such that 2 <= n <= 10^4, and `n` is not equal to 2; `max_index` is n-1.
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        
        if res == '<':
            min_indices = [i]
        elif res == '=':
            min_indices.append(i)
        
    #State: `n` is an integer such that 2 <= n <= 10^4, and `n` is not equal to 2; `max_index` is n-1; `min_indices` is a list containing all indices that are considered equal to `max_index` by `func_1`.
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        
        res = func_1(min_index, min_index, min_index, i)
        
        if res == '=':
            min_index = i
        
    #State: - `n` remains unchanged.
    #- `max_index` remains unchanged.
    #- `min_indices` remains unchanged.
    #- `min_index` will either remain the same (if no other index in `min_indices` causes `func_1` to return `'='`) or be updated to the first index `i` in `min_indices` (other than `max_index`) for which `func_1(min_index, min_index, min_index, i)` returns `'='`.
    #
    #Since the problem does not specify the behavior of `func_1` or provide more details about the contents of `min_indices`, we can only conclude that `min_index` will be updated based on the condition described.
    #
    #Output State:
    func_2(max_index, min_index)
#Overall this is what the function does:The function `func_3` reads an integer `n` from the input, performs a series of operations involving comparisons (using `func_1`), and then calls `func_2` with two indices (`max_index` and `min_index`). The function itself does not return any value (returns `None`).

